import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="MedBot", page_icon="🏥", layout="centered")

st.title("🏥 MedBot")
st.caption("Your friendly health helper")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm MedBot. Tell me your symptoms and I'll help! 😊"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("What's bothering you?")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = get_response(user_input)
            st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

st.markdown("---")
st.caption("⚠️ Not a substitute for professional medical advice")
