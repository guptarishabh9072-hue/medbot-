import streamlit as st
from datetime import datetime
from chatbot import get_response
from prompts import QUICK_SYMPTOMS

st.set_page_config(page_title="MedBot", page_icon="🏥", layout="centered")

st.title("🏥 MedBot")
st.caption("Your friendly health assistant 💙")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm MedBot 👋 Tell me your symptoms and I'll help! You can also tap a quick button below."}
    ]
    st.session_state.wizard_step = 0
    st.session_state.wizard_answers = {}
    st.session_state.history = []

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.header("📋 Quick Symptoms")
    for emoji_label, symptom in QUICK_SYMPTOMS.items():
        if st.button(emoji_label, use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": symptom})
            with st.chat_message("user"):
                st.write(symptom)
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    reply = get_response(symptom)
                    st.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
            st.rerun()

    st.markdown("---")
    st.header("🔍 Symptom Checker")
    if st.button("Start Wizard", use_container_width=True):
        st.session_state.wizard_step = 1
        st.session_state.wizard_answers = {}

    st.markdown("---")
    st.header("📁 Chat History")
    if st.session_state.history:
        for i, item in enumerate(st.session_state.history[-5:]):
            st.caption(f"{i+1}. {item['symptom'][:30]}... - {item['time']}")
    else:
        st.caption("No history yet")

    st.markdown("---")
    st.header("🗣️ Voice Input")
    audio_value = st.audio_input("Speak your symptoms")
    if audio_value:
        st.session_state.messages.append({"role": "user", "content": audio_value})
        with st.chat_message("user"):
            st.write(audio_value)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                reply = get_response(audio_value)
                st.write(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm MedBot 👋 Tell me your symptoms and I'll help!"}
        ]
        st.rerun()

if st.session_state.get("wizard_step", 0) > 0:
    from prompts import WIZARD_QUESTIONS
    step = st.session_state.wizard_step - 1
    if step
