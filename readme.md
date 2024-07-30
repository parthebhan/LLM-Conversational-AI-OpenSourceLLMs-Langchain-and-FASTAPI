# **Extending Conversational AI: Open Source LLMs, Langchain, and FASTAPI**

## LLM Models:
- `1. Gemini-1.5-pro-latest`
- `2. Llama3-8b-8192`

# app.py

## Purpose:
The Python script sets up a FastAPI server that integrates with Google's Generative AI (Gemini model) and Groq to generate responses based on user queries.

## Libraries Used:
- `FastAPI`: For building the API endpoints and server.
- `langchain.prompts.ChatPromptTemplate`: Template for generating prompts.
- `langchain_google_genai.GoogleGenerativeAI`: Interface for using Google's Generative AI models.
- `langchain_groq.ChatGroq`: Interface for using Groq models.
- `groq.Groq`: Groq client for API interactions.
- `uvicorn`: ASGI server for running FastAPI applications.
- `os`: For environment variables (`GOOGLE_API_KEY`, `GROQ_API_KEY`) management.
- `dotenv`: For loading environment variables from a `.env` file.
- `json`: For handling JSON data.

## Components of the Script:

### 1. Loading Environment Variables:
   - Uses `dotenv` to load environment variables (`GOOGLE_API_KEY` and `GROQ_API_KEY`).

### 2. FastAPI Application Setup:
   - Initializes a FastAPI application named "Langchain Server" with version 1.1 and a description indicating it's a simple API Server.

### 3. Model Initialization:
   - Initializes **`GoogleGenerativeAI` model (`gemini-1.5-pro-latest`)** and **`ChatGroq` model (`llama3-8b-8192`)** using the respective API keys obtained from environment variables.

### 4. API Endpoints:
   - `/chat_google`: GET endpoint that generates responses using Google's Generative AI based on user queries.
   - `/chat_groq`: GET endpoint that generates responses using Groq based on user queries.

### 5. Server Execution:
   - If the script is run directly (`__name__ == "__main__"`), starts the FastAPI server using `uvicorn` on `localhost:8000`.

## Usage:
To use the script:
- Ensure Python dependencies (`FastAPI`, `uvicorn`, `langchain`, `langchain_google_genai`, `langchain_groq`, `dotenv`) are installed.
- Obtain Google and Groq API keys (`GOOGLE_API_KEY` and `GROQ_API_KEY`) and store them in a `.env` file.
- Run the script using `uvicorn app:app --reload` in the terminal.
- Navigate to `http://localhost:8000/docs` to interact with the API endpoints.

---

# client.py

## Purpose:
This Streamlit application interacts with a FastAPI server that integrates with Google's Generative AI (Gemini model) and Groq to generate responses based on user queries.

## Components of the Script:

### 1. Functionality:
   - Allows users to input queries to generate responses using Google's Generative AI and Groq via a FastAPI server.
   - Communicates with the FastAPI server hosted at `BASE_URL` (`http://localhost:8000`).

### 2. User Interface:
   - **Title**: Displays a title indicating the integration of conversational AI models and FastAPI.
   - **Chat with Google Generative AI**: Section for users to input queries and generate responses using Google's Generative AI.
   - **Chat with Groq**: Section for users to input queries and generate responses using Groq.
   - **Response Time**: Displays the time taken for the server to generate responses.
   - **Error Handling**: Displays appropriate error messages if there are issues with generating responses.

## Usage:
To use the Streamlit application:
- Ensure Python dependencies (`streamlit`, `requests`, `time`) are installed.
- Run the Streamlit application using `streamlit run app_streamlit.py` in the terminal.
- Interact with the UI to input queries and generate responses using Google's Generative AI or Groq via the FastAPI server.

---

## 🔗 Connect with Me

Feel free to connect with me on LinkedIn:

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://parthebhan143.wixsite.com/datainsights)

[![LinkedIn Profile](https://img.shields.io/badge/LinkedIn_Profile-000?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/parthebhan)

[![Kaggle Profile](https://img.shields.io/badge/Kaggle_Profile-000?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/parthebhan)

[![Tableau Profile](https://img.shields.io/badge/Tableau_Profile-000?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/parthebhan.pari/vizzes)


