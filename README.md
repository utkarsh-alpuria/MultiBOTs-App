# 🤖 MultiBOTs-App

A **Streamlit** app featuring various **LLM-based chatbots** designed to interact with users in different ways.

## 📂 About the Files

- **`AskBot.py`**: The main entry point of the app. This is the initial UI you see when you launch the app, providing a basic chatbot where you can ask queries.

- **`.env`**: Contains environmental variables, including API keys required for accessing various services.

- **`requirements.txt`**: Lists all the dependencies and modules needed for the project.

- **`pages/1_ChatBot.py`**: A chatbot accessible from the sidebar UI. This bot can engage in conversations and remember context.

- **`pages/2_PDF-Bot.py`**: A specialized bot that allows you to upload a PDF file and ask questions related to its content.
  
- **`pages/3_Tool-Bot.py`**: A tool/function calling bot that use google generative AI function calling to tell current weather and news.

## 🚀 Get Started with the Project

1. Ensure Python is installed on your machine.
2. Clone the project repository or download the zip file.
3. Open the project folder in VS Code or any other IDE.
4. Create a virtual environment using:
   ```bash
   python -m venv <name_of_virtual_environment>
   ```
5. Activate the virtual environment:
   - On Windows:
     ```bash
     .\<name_of_virtual_environment>\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source <name_of_virtual_environment>/bin/activate
     ```
6. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

7. **Create Accounts** on the following platforms:
   - [Hugging Face](https://huggingface.co/)
   - [Cohere](https://cohere.com/)
   - [LangChain](https://www.langchain.com/)
   - [Google AI Studio](https://ai.google.dev/aistudio)
   - [OpenWeatherMap](https://openweathermap.org/)
     
   Generate your personal API keys or tokens on all platforms.

8. **Configure API Keys**:
   - Copy your Hugging Face API token, Cohere API key, and LangChain API key.
   - Open the `.env` file and replace `"your HuggingFace API key"`, `"your Cohere API key"`, `"your LangChain API key"`, `"your Google API key"` and `"your WeatherMap API key"` with your actual keys or token as strings. Save the changes.

9. **Run the App**:
   Ensure you are in the project directory and execute:
   ```bash
   streamlit run AskBot.py
   ```

10. **the App** will launch automatically in the browser.

11. If not you will get a `http://localhost:port` link in the terminal, just open that link in the browser.
