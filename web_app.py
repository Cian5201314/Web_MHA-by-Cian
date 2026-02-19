import streamlit as st

# Setup the page appearance
st.set_page_config(page_title="Mental Health Check", page_icon="🧠", layout="centered")

# --- 1. INITIALIZE MEMORY (SESSION STATE) ---
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

# --- 2. THE QUESTIONS & OPTIONS ---
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

st.title("Mental Health Check-In")

# --- 3. DISPLAY LOGIC ---

# If we haven't finished all 21 questions yet:
if st.session_state.current_q < len(questions):
    
    # Progress Bar
    progress_percent = st.session_state.current_q / len(questions)
    st.progress(progress_percent)
    st.write(f"**Question {st.session_state.current_q + 1} of 21**")
    st.divider()
    
    # Show the current question
    current_question_text = questions[st.session_state.current_q]
    st.subheader(current_question_text)
    
    # Get the user's choice
    choice = st.radio("Select how much this applied to you over the past week:", options, index=None)
    
    st.divider()
    
    # Next Button
    if st.button("Next", type="primary"):
        if choice is None:
            st.warning("Please select an answer before continuing.")
        else:
            # Save the score (0, 1, 2, or 3)
            score = options.index(choice)
            st.session_state.answers.append(score)
            
            # Move to the next question
            st.session_state.current_q += 1
            st.rerun()

# If all questions are answered, calculate and show results:
else:
    st.success("You've completed the check-in!")
    st.balloons() # Adds a nice visual celebration
    
    # --- 4. YOUR SCORING BACKBONE ---
    r = [0] + st.session_state.answers
    
    d_total = r[3] + r[5] + r[10] + r[13] + r[16] + r[17] + r[21]
    a_total = r[2] + r[4] + r[7] + r[9] + r[15] + r[19] + r[20]
    s_total = r[1] + r[6] + r[8] + r[11] + r[12] + r[14] + r[18]
    
    d_score = d_total * 2
    a_score = a_total * 2
    s_score = s_total * 2

    def get_label(score, cutoffs):
        if score <= cutoffs[0]: return "Normal"
        elif score <= cutoffs[1]: return "Mild"
        elif score <= cutoffs[2]: return "Moderate"
        elif score <= cutoffs[3]: return "Severe"
        else: return "Extremely Severe"

    d_result = get_label(d_score, [9, 13, 20, 27])
    a_result = get_label(a_score, [7, 9, 14, 19])
    s_result = get_label(s_score, [14, 18, 25, 33])

    st.subheader("Your Results")
    col1, col2, col3 = st.columns(3)
    col1.metric("Depression", f"{d_score}", d_result, delta_color="off")
    col2.metric("Anxiety", f"{a_score}", a_result, delta_color="off")
    col3.metric("Stress", f"{s_score}", s_result, delta_color="off")
    
    st.info("I will be here for you anytime you want. If you feel down, come back anytime!")
    
    # Add a button to restart the test
    if st.button("Start Over"):
        st.session_state.current_q = 0
        st.session_state.answers = []
        st.rerun()
