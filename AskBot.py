# Ask-BOT using open source HuggingFace and Cohere LLM

# Module imports
from langchain import HuggingFaceHub, LLMChain, PromptTemplate
from dotenv import load_dotenv
import streamlit as st
from langchain import Cohere
import os


load_dotenv() # take environment variables from .env(here llm api key and langchain api key)

# Function to load llm model form huggingface and get response
# def get_llm_response(query):
#     llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature":0, "max_length":64}) # using model from repo_id
#     response = llm.predict(query)
#     return response


# Function to load llm model form cohere and get response
def get_cohere_response(input_prompt):
    cohere_llm = Cohere(cohere_api_key=os.environ["COHERE_API_KEY"])
    response = cohere_llm.invoke(input_prompt)
    return response

# print(get_cohere_response("what is the capital of India"))
    
# initialize streamlit app
st.set_page_config(page_title="Chatbot - LLM")
st.title("Ask-BOT :robot_face:")
st.markdown("---")


input = st.text_input("##### :blue[Input Query :]", key="input", placeholder="click to enter query")


submit = st.button("Ask Query", type="primary")

if submit:
    st.markdown("##### :orange[AskBot...]")
    response = get_cohere_response(input)
    st.write(response)