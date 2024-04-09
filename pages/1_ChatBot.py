# Chat-BOT 

from langchain_cohere import ChatCohere
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv() ## take environment variables from .env(langchain api key, cohere api key)

# For LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true" 


# Streamlit Page
st.set_page_config(page_title="Q&A chatbot")
st.title("Chat-BOT :large_green_circle:")
st.markdown("---")


# ChatCohere llm
ChatCohere_llm = ChatCohere(cohere_api_key=os.environ["COHERE_API_KEY"], temperature=0.5)


# Get response message function
# create session state to keep the chat flow for model as memory
if "chat_flow" not in st.session_state:
    st.session_state["chat_flow"] = [SystemMessage(content="You are a chatting AI assistant")]

def get_ChatCohere_response(human_question):

    st.session_state["chat_flow"].append(HumanMessage(content=human_question))
    ai_answer = ChatCohere_llm(st.session_state["chat_flow"])
    st.session_state["chat_flow"].append(AIMessage(content=ai_answer.content))
    return ai_answer.content

# Chat Area UI
outer_container = st.container(border=True)
with outer_container:
    chat_container = st.container(border=False)
    with chat_container:
        for message in st.session_state['chat_flow']:
            if message.type == "system":
                sy_message_area = st.columns([8,4])
                with sy_message_area[0]:
                    sy_mess_con = st.container(border=True)
                    sy_mess_con.write(":green[Chat-BOT...]")
                    sy_mess_con.write("Hello! how can I help you?") 

            elif message.type == "human":
                human_message_area = st.columns([4,8])
                with human_message_area[1]:
                    hu_mess_con = st.container(border=True)
                    hu_mess_con.write(":blue[You...]")
                    hu_mess_con.write(message.content)

            else:
                ai_message_area = st.columns([8,4])
                with ai_message_area[0]:
                    ai_mess_con = st.container(border=True)
                    ai_mess_con.write(":green[Chat-BOT...]")
                    ai_mess_con.write(message.content)                            
    # message area UI    
    input_grid = st.columns([13,2])
    with input_grid[0]:
        human_input = st.text_input("Chat here", key="human_input", label_visibility="collapsed", placeholder="Message Chat-BOT...")
    with input_grid[1]:
        send_button=st.button("Send :arrow_forward:", type="primary")

if send_button:
    ChatCohere_response = get_ChatCohere_response(human_input)
    st.rerun()

    