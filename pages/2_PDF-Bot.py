# PDF-BOT

from langchain import HuggingFaceHub, LLMChain, PromptTemplate
from dotenv import load_dotenv
import streamlit as st
from langchain_cohere import ChatCohere
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import CohereEmbeddings
import os


load_dotenv()

# Streamlit UI
st.set_page_config("PDF-BOT")
st.title("PDF-BOT :page_facing_up:")
st.markdown("---")

pdf_file = st.file_uploader("##### :orange[Upload a PDF]", type=[".pdf"])

outer_containeer = st.container(border=True)
with outer_containeer:
    st.write(":blue[Aske your Question]")
    question_grid = st.columns([14,2])
    with question_grid[0]:
        human_question = st.text_input("Ask here", key="human_input", label_visibility="collapsed", placeholder="Question related to PDF")
    with question_grid[1]:
        ask_button=st.button("Ask :arrow_forward:", type="primary")

# function to convert pdf data to text chunks
if pdf_file:
    pdf_reader_obj = PdfReader(pdf_file)
    combined_text = ""
    for page in pdf_reader_obj.pages:
        combined_text += page.extract_text()


    # Creating LangChain embeddings and LLM objects
    ChatCohere_llm = ChatCohere(cohere_api_key=os.environ["COHERE_API_KEY"])
    cohere_embeddings = CohereEmbeddings()

    # creatinf text_chunks from combined_text
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 500,
        chunk_overlap = 100,
        length_function = len,
    )
    text_chunks = text_splitter.split_text(combined_text)

    # st.write(text_chunks) --> list



if ask_button:
    if human_question:
        # Creating VectorStore
        vector_store = DocArrayInMemorySearch.from_texts(
            text_chunks,
            embedding= cohere_embeddings
        )
        retriever = vector_store.as_retriever()

        # Creating Prompt    
        template = """Answer the question based only on the following context:
        {context}
        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(template=template)
        output_parser = StrOutputParser()

        # combining context and question
        setup_and_retrival = RunnableParallel(
            {"context": retriever, "question": RunnablePassthrough()}
        )

        # creating chain to generate answer(output)
        chain = setup_and_retrival | prompt | ChatCohere_llm | output_parser

        answer = chain.invoke(human_question) # invoking chain

        ansewer_container = st.container(border=True, height= 200)
        with ansewer_container:
            st.write("##### :green[PDF-Bot...]")
            st.write(answer)