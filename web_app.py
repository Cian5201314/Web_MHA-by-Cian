import streamlit as st

# Setup the page appearance
st.set_page_config(page_title="Mental Health Check", page_icon="🧠", layout="centered")

st.markdown("""
<style>
    html, body, [class*="st-"] {
        font-family: 'Umoe', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. INITIALIZE MEMORY (SESSION STATE) ---
if 'started' not in st.session_state:
    st.session_state.started = False  # Tracks if they are on the landing page
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

# --- 2. THE QUESTIONS & OPTIONS ---
questions = [
    "၁။ ကျွန်ပ်သည် စိတ်အေးလက်အေးနေဖို့ခက်ခဲခဲ့သည်။",
    "၂။ ကျွန်ပ်သည် အာခေါင်ခြောက်တတ်သည်ကို သတိထားမိခဲ့သည်။",
    "၃။ ကျွန်ုပ် ဘာကိုမှ အကောင်းမြင်၍ မရပါ။",
    "၄။ ကျွန်ုပ်သည် ပင်ပင်ပန်းပန်းမလုပ်ပါဘဲ အသက်ရှူမဝသလို၊ အသက်ရှူမြန်သလို ခံစားခဲ့ရသည်။",
    "၅။ ကျွန်ပ်သည် လုပ်စရာရှိသည်များကို ဦးအောင်လုပ်ဖို့ (စတင်ဖို့) ခက်ခဲခဲ့သည်။",
    "၆။ ကျွန်ပ်သည် အခြေအနေများကို လိုအပ်သည်ထက်ပို၍ ပြင်းထန်စွာတုံ့ပြန်တတ်သည်။",
    "၇။ ကျွန်ုပ်သည် ကတုန်ကယင်ဖြစ်သလို ခံစားခဲ့ရသည်။ (ဥပမာ၊ လက်တုန်ခြင်း)",
    "၈။ ကျွန်ုပ်သည် စိတ်လှုပ်ရှားပြီး အင်အားများစွာစိုက်ထုတ်နေခဲ့ရသည်ဟု ခံစားရသည်။",
    "၉။ ကျွန်ုပ်သည် စိတ်လှုပ်ရှား ကြောက်ရွံ့လွန်းပြီး ကြောင်တောင်တောင်ပြုမူလိုက်မိမည်ကိုစိုးရိမ်နေခဲ့မိသည်။",
    "၁၀။ ရှေ့လျှောက် ကျွန်ပ်အတွက် ဘာမှ မျှော်ကိုးစရာ မရှိတော့ဟု ခံစားသည်။",
    "၁၁။ ကျွန်ပ် စိတ်အနှောက်အယှက်ဖြစ်လွယ်သည်။",
    "၁၂။ ကျွန်ုပ်သည် စိတ်ကိုဖြေလျှော့၍ ပေါ့ပေါ့ပါးပါးနေရန် ခက်ခဲခဲ့သည်။",
    "၁၃။ ကျွန်ုပ်သည် စိတ်ပျက်အားလျော့သလို၊ စိတ်ဓာတ်ကျသလို ခံစားခဲ့ရသည်။",
    "၁၄။ ကျွန်ုပ် လုပ်ဆောင်နေသည့်အရာများ ရှေ့ဆက်မရအောင် အဟန့်အတားဖြစ်စေသည့် အရာများကို သည်းမခံနိုင်ခဲ့ပါ။",
    "၁၅။ ကျွန်ုပ်သည် ရုတ်တရက် စိုးရိမ်ထိတ်လန့်ပြီး စိတ်လွတ်လုနီးပါး ခံစားခဲ့ရသည်။",
    "၁၆။ ကျွန်ပ်သည် အရာအားလုံးနီးပါးတွင် စိတ်ဝင်စားမှုလျော့ပါးနေသည်။",
    "၁၇။ ကျွန်ုပ်သည် မိမိကိုယ်ကိုယ် တန်ဖိုးမရှိသူတစ်ယောက်ကဲ့သို့ ခံစားရသည်။",
    "၁၈။ ကျွန်ပ်သည် မိမိကိုယ်ကိုယ် စိတ်ဆတ်လာသည်ဟု ခံစားရသည်။",
    "၁၉။ ကျွန်ပ်သည် ကိုယ်လက်လှုပ်ရှားမှု မရှိပါပဲ နှလုံးခုန်မြန်နေတတ်သည်။",
    "၂၀။ ကျွန်ပ်သည် အကြောင်းပြချက်ကောင်းကောင်းမရှိပဲ ကြောက်ရွံ့နေသည်။",
    "၂၁။ ကျွန်ုပ်၏ ဘဝသည် အဓိပ္ပါယ်မရှိဟု ခံစားခဲ့ရသည်။"
]

options = [
    "0: လုံးဝမဖြစ်ပါ။",
    "1: တခါတရံ ဖြစ်သည်။",
    "2: အမြဲ မဟုတ်၊ မကြာခဏဖြစ်သည်။",
    "3: အမြဲဖြစ်သည်၊ အလွန်အမင်းဖြစ်သည်။"
]

# --- 3. DISPLAY LOGIC ---

# FRONT PAGE
if not st.session_state.started:
    st.markdown('<h1 class="custom-title">စိတ်ကျခြင်း၊ စိတ်ပူပန်ခြင်းနှင့် စိတ်ဖိစီးခြင်းတို့အတွက် မိမိကိုယ်တိုင် အမှတ်ပေးစနစ်ဖြင့်အမှတ်တွက်၍ ဆန်းစစ်လေ့လာခြင်း</h1>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Notice how these are now single continuous lines in the code
    st.write("စိတ်ကျန်းမာရေးကို ဂရုစိုက်ခြင်းသည် ခန္ဓာကိုယ်ကျန်းမာရေးကို ဂရုစိုက်သကဲ့သို့ ထပ်တူအရေးကြီးပါသည်။ ဤ စိတ်ကျခြင်း၊ စိတ်ပူပန်ခြင်းနှင့် စိတ်ဖိစီးခြင်းတို့အတွက် အမှတ်ပေးစနစ်ဖြင့် အမှတ်တွက်၍ ဆန်းစစ်လေ့လာခြင်းမေးခွန်းများကို ဖြေဆိုပြီးလျှင် သင့်ရမှတ်ကို တွက်ချက်ပေးပါမည်။")
    st.write("မေးခွန်း ၂၁ ခုပါရှိပါမည်။ စာကြောင်းတိုင်းကိုဖတ်၍ လွန်ခဲ့သော တစ်ပတ်အတွင်း သင်မည်သို့ခံစားရသည်ကို ဖြေဆိုပါ။ အဖြေ မှန်/မှား ဟူ၍ မရှိပါ။ အချိန်ကြာမြင့်စွာ မစဉ်းစားပါနှင့်။")
    st.write("*(ဤဆန်းစစ်ချက်မှ ရရှိလာသော အဖြေရလာဒ်များသည် ယေဘုယျ ခန့်မှန်းတွက်ချက်မှုများသာဖြစ်ပြီး မိမိတွင် အမှန်တကယ် စိတ်ကျရောဂါ၊ စိတ်ပူပန်မှုနှင့် စိတ်ဖိစီးမှုအခြေအနေများ ရှိ/မရှိ နှင့် ပြင်းထန်/မပြင်းထန် စသည်တို့အတွက် စိတ်ကျန်းမာရေးဆရာဝန်နှင့် အသေးစိတ် တိုင်ပင်ဆွေးနွေးရန် လိုအပ်ပါသည်)*")
    
    st.divider()
    
    if st.button("မေးခွန်းတွေစဖြေမည်။"):
        st.session_state.started = True
        st.rerun()

# THE QUIZ
else:
    #st.title("Mental Health Check-In")
    
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
        choice = st.radio("လွန်ခဲ့သော တစ်ပတ်အတွင်း သင်မည်သို့ခံစားရသည်ကို ဖြေဆိုပါ။", options, index=None,key=f"radio_q_{st.session_state.current_q}")
        
        st.divider()
        
        # Next Button
        if st.button("Next", type="primary"):
            if choice is None:
                st.warning("အဖြေတခုကိုရွေးပါ")
            else:
                # Save the score (0, 1, 2, or 3)
                score = options.index(choice)
                st.session_state.answers.append(score)
                
                # Move to the next question
                st.session_state.current_q += 1
                st.rerun()
    
    # If all questions are answered, calculate and show results:
    else:
        st.success("ဖြေဆိုစစ်ဆေးမှု ပြီးပါပြီ။")
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
            if score <= cutoffs[0]: return "ပုံမှန်"
            elif score <= cutoffs[1]: return "အပျော့စား"
            elif score <= cutoffs[2]: return "အသင့်အတင့်"
            elif score <= cutoffs[3]: return "ပြင်းထန်"
            else: return "အလွန်ပြင်းထန်"
    
        d_result = get_label(d_score, [9, 13, 20, 27])
        a_result = get_label(a_score, [7, 9, 14, 19])
        s_result = get_label(s_score, [14, 18, 25, 33])
    
        st.subheader("သင့်အမှတ်ပေါင်း")
        col1, col2, col3 = st.columns(3)
        col1.metric("သင်၏ စိတ်ဓာတ်ကျခြင်း (Depression) ရမှတ်ပေါင်းမှာ", f"{d_score}", d_result, delta_color="off")
        # Fixed the labels here to match Anxiety (a_score) and Stress (s_score)
        col2.metric("သင်၏ စိုးရိမ်စိတ်များခြင်း (Anxiety) ရမှတ်ပေါင်းမှာ", f"{a_score}", a_result, delta_color="off")
        col3.metric("သင်၏ စိတ်ဖိစီးခြင်း (Stress) ရမှတ်ပေါင်းမှာ", f"{s_score}", s_result, delta_color="off")
        
        st.info("သင့်အမှတ်ပေါင်းသည် ပြင်းထန် (သို့) အလွန်ပြင်းထန် အပိုင်းအခြားအတွင်း ရောက်နေလျှင် စိတ်ကျန်းမာရေးဆရာဝန်နှင့် မဖြစ်မနေ ချက်ချင်း ဆွေးနွေးတိုင်ပင်သင့်ပါသည်။")
        st.info("စိတ်ကျန်းမာရေးအတွက် ဆွေးနွေးမှုရယူရန် တယ်လီကျန်းမာ မက်ဆင်ဂျာ (https://m.me/telehealthmm) သို့မဟုတ် တယ်လီဂရမ် (https://t.me/TLKMReception) သို့ အခုပဲဆက်သွယ်ပြီး ဘိုကင်ယူလိုက်ပါ။")
        st.info("အထက်ပါ သင့်ဖြေဆိုမှုများကို ယခုအချိန်အထိ တယ်လီကျန်းမာသို့ ပေးပို့ထားခြင်း မရှိသေးပါ။ သို့ဖြစ်ပါ၍ သင့်အဖြေများကို ပေးပို့လိုခြင်းမရှိပါက ယခုမေးခွန်းလွှာကို ပိတ်လိုက်နိုင်ပါသည်။ သို့မဟုတ် screenshot ရိုက်ယူထားပြီး စိတ်ကျန်းမာရေး ဆွေးနွေးမှုတွင် အသုံးပြုနိုင်ပါသည်။")
        
        # Add a button to restart the test
        if st.button("ပြန်စမည်"):
            st.session_state.started = False # Send them back to the front page
            st.session_state.current_q = 0
            st.session_state.answers = []
            st.rerun()
