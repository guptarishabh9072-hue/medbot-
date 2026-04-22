import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="MedBot", page_icon="🏥")

st.title("🏥 MedBot")

# Add sidebar with info
with st.sidebar:
    st.header("About MedBot")
    st.info(
        "⚠️ **Important**: This is not a replacement for professional medical advice. "
        "Always consult with a qualified healthcare provider."
    )
    
    st.header("Emergency Symptoms")
    st.warning(
        "🚨 **Seek immediate medical help if you experience:**\n"
        "- Chest pain\n"
        "- Difficulty breathing\n"
        "- Severe bleeding\n"
        "- Loss of consciousness\n"
        "- High fever (>103°F/39.4°C)"
    )
    
    if st.button("Clear Chat"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello, I'm MedBot. Please describe your symptoms."}
        ]
        st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello, I'm MedBot. Please describe your symptoms."}
    ]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if user_input := st.chat_input("Describe your symptoms..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = get_response(user_input)
            st.write(reply)
    
    # Add assistant response
    st.session_state.messages.append({"role": "assistant", "content": reply})

# Footer
st.markdown("---")
st.caption("🏥 MedBot - Your AI Health Assistant (Not a substitute for professional medical advice)")