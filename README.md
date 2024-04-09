# MultiBOTs-App
Streamlit App with LLM based chatbots.

### About files: ###

#### AskBot.py ####

This file is like the main page of the app, when you launch the App this is the first UI you will see. A basic bot where you can ask quries.

#### .env ####

This has the environmental variables(API keys) 

#### pages/1_ChatBot.py ####

This is another bot you can access from the side bar of UI. Capable of having a chat conversation remembering the context.

#### pages/2_PDF-Bot.py ####

This is a bot where you can upload a pdf file and ask question related to the text in pdf file.

### How to Run? ###
1) Clone the project
2) Open project folder in code editor
3) In code editor terminal run command pip install -r requirements.txt
4) Create account <https://huggingface.co/> , <https://cohere.com/> and <https://www.langchain.com/> and generate your personal Api keys or token in all the platforms.
5) Copy your created (HuggingFace Api token), (Cohere Api key) and (LangChain Api key) from the platforms and inside .env file replace "your HuggingFace api key", "your Cohere api key" and "your LangChain api key" respectively as strings and save the changes.
6) In terminal check that you are in the project folder and run command streamlit run .\AskBot.py
7) you will see the app will launch it the browser.


