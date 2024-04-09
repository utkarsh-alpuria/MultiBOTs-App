### MultiBOTs-App

A Streamlit App featuring LLM-based chatbots.

#### About Files:

- *AskBot.py*: This serves as the main page of the app. When you launch the app, this is the initial UI you encounter. It provides a basic bot where you can ask queries.

- *.env*: This file contains environmental variables such as API keys.

- *pages/1_ChatBot.py*: Another bot accessible from the sidebar of the UI. It can engage in chat conversations and remember context.

- *pages/2_PDF-Bot.py*: This bot allows you to upload a PDF file and ask questions related to its content.

### How to Run?

1. Clone the project.
2. Open the project folder in a code editor.
3. In the code editor terminal, run the command pip install -r requirements.txt.
4. Create accounts on [Hugging Face](https://huggingface.co/), [Cohere](https://cohere.com/), and [LangChain](https://www.langchain.com/), and generate your personal API keys or tokens on all platforms.
5. Copy your created HuggingFace API token, Cohere API key, and LangChain API key from the platforms. Inside the .env file, replace "your HuggingFace API key", "your Cohere API key", and "your LangChain API key" respectively as strings, and save the changes.
6. In the terminal, ensure that you are in the project folder, and run the command streamlit run AskBot.py.
7. The app will launch in your browser.


