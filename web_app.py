import streamlit as st

# Setup the page appearance
st.set_page_config(page_title="Mental Health Check", page_icon="🧠", layout="centered")

st.title("Mental Health Check-In")
st.write("Please read each statement and select how much it applied to you **over the past week**.")
st.divider()

# The 21 Questions
questions = [
    "1. I found it hard to wind down.",
    "2. I was aware of dryness of my mouth.",
    "3. I couldn't seem to experience any positive feeling at all.",
    "4. I experienced breathing difficulty.",
    "5. I found it difficult to work up the initiative to do things.",
    "6. I tended to over-react to situations.",
    "7. I experienced trembling (e.g., in the hands).",
    "8. I felt that I was using a lot of nervous energy.",
    "9. I was worried about situations in which I might panic and make a fool of myself.",
    "10. I felt that I had nothing to look forward to.",
    "11. I found myself getting agitated.",
    "12. I found it difficult to relax.",
    "13. I felt down-hearted and blue.",
    "14. I was intolerant of anything that kept me from getting on with what I was doing.",
    "15. I felt I was close to panic.",
    "16. I was unable to become enthusiastic about anything.",
    "17. I felt I wasn't worth much as a person.",
    "18. I felt that I was rather touchy.",
    "19. I was aware of the action of my heart in the absence of physical exertion.",
    "20. I felt scared without any good reason.",
    "21. I felt that life was meaningless."
]

options = [
    "0: Did not apply to me at all",
    "1: Applied to me to some degree",
    "2: Applied to me to a considerable degree",
    "3: Applied to me very much"
]

# Create a form so the app doesn't refresh until the user clicks "Submit"
with st.form("dass21_form"):
    responses = []
    for q in questions:
        # Display the radio buttons and save the index (0, 1, 2, or 3)
        choice = st.radio(q, options, index=0)
        responses.append(options.index(choice))
    
    st.divider()
    submitted = st.form_submit_button("Calculate My Score", type="primary")

# --- YOUR SCORING BACKBONE ---
if submitted:
    # Add a dummy 0 at the start so indices match your r1 to r21 logic
    r = [0] + responses
    
    d_total = r[3] + r[5] + r[10] + r[13] + r[16] + r[17] + r[21]
    a_total = r[2] + r[4] + r[7] + r[9] + r[15] + r[19] + r[20]
    s_total = r[1] + r[6] + r[8] + r[11] + r[12] + r[14] + r[18]
    
    d_score = d_total * 2
    a_score = a_total * 2
    s_score = s_total * 2

    # Determine Text Results
    def get_label(score, cutoffs):
        if score <= cutoffs[0]: return "Normal"
        elif score <= cutoffs[1]: return "Mild"
        elif score <= cutoffs[2]: return "Moderate"
        elif score <= cutoffs[3]: return "Severe"
        else: return "Extremely Severe"

    d_result = get_label(d_score, [9, 13, 20, 27])
    a_result = get_label(a_score, [7, 9, 14, 19])
    s_result = get_label(s_score, [14, 18, 25, 33])

    # Display Results beautifully
    st.subheader("Your Results")
    col1, col2, col3 = st.columns(3)
    col1.metric("Depression", f"{d_score}", d_result, delta_color="off")
    col2.metric("Anxiety", f"{a_score}", a_result, delta_color="off")
    col3.metric("Stress", f"{s_score}", s_result, delta_color="off")
    
    st.info("I will be here for you anytime you want. If you feel down, come back anytime!")