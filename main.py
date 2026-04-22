import streamlit as st
from core.bot import get_response

st.set_page_config(page_title="MedBot", page_icon="🏥")
st.markdown("""
<style>
    .stApp { background: #fafafa; }
    .stTextInput>div>div>input { border-radius: 20px; padding: 12px 16px; }
    div[data-testid="stChatMessage"] { padding: 8px 0; }
</style>
""", unsafe_allow_html=True)

st.title("🏥 MedBot")
st.caption("Your health helper")

if "msgs" not in st.session_state:
    st.session_state.msgs = [{"role": "bot", "text": "Hi! Tell me your symptoms."}]

for m in st.session_state.msgs:
    st.chat_message(m["role"]).write(m["text"])

if msg := st.chat_input("Describe symptoms..."):
    st.session_state.msgs.append({"role": "user", "text": msg})
    with st.chat_message("user"):
        st.write(msg)
    
    with st.chat_message("bot"):
        with st.spinner("..."):
            reply = get_response(msg)
            st.write(reply)
    st.session_state.msgs.append({"role": "bot", "text": reply})

st.caption("⚠️ Not medical advice. Consult a doctor.")