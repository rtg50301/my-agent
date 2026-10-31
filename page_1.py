import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_tavily import TavilySearch

load_dotenv()

tool = TavilySearch(
    max_results=5,
    topic="general",
    # include_answer=False,
    # include_raw_content=False,
    # include_images=False,
    # include_image_descriptions=False,
    # search_depth="basic",
    # time_range="day",
    # include_domains=None,
    # exclude_domains=None
)

model = init_chat_model("gpt-5.4-mini")
agent = create_agent(model, [tool])

# 도구 생성

st.title('page1')

if 'messages' not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("Say something")

if prompt:
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    response = agent.invoke(
        {"messages": [{"role": "user", "content": prompt}]}
    )
    st.session_state.messages.append({'role': 'ai', 'content': response['messages'][-1].content})

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])