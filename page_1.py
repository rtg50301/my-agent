import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
model = init_chat_model("gpt-5.4-mini")

st.title('page1')

if 'messages' not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("Say something")

if prompt:
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    response = model.invoke(prompt)
    st.session_state.messages.append({'role': 'ai', 'content': response.content})

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])