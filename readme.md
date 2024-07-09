# FastAPI Server with Google Generative AI Integration

### Purpose:
The Python script sets up a FastAPI server that integrates with Google's Generative AI (Gemini model) to generate essays based on user-provided topics.

### Libraries Used:
- `FastAPI`: For building the API endpoints and server.
- `langchain.prompts.ChatPromptTemplate`: Template for generating prompts.
- `langchain_google_genai.GoogleGenerativeAI`: Interface for using Google's Generative AI models.
- `uvicorn`: ASGI server for running FastAPI applications.
- `os`: For environment variables (`GOOGLE_API_KEY`) management.
- `dotenv`: For loading environment variables from a `.env` file.
- `json`: For handling JSON data.

### Components of the Script:

1. **Loading Environment Variables**:
   - The script uses `dotenv` to load environment variables, particularly `GOOGLE_API_KEY` which is required for authentication with Google's API.

2. **FastAPI Application Setup**:
   - Initializes a FastAPI application named "Langchain Server" with version 1.0 and a description indicating it's a simple API server.

3. **Google Generative AI Model Initialization**:
   - Creates an instance of `GoogleGenerativeAI` model (`gemini-1.5-pro-latest`) using the `google_api_key` obtained from the environment variables.

4. **API Endpoint for Essay Generation (`/essay`)**:
   - Defines a GET endpoint `/essay` that accepts a query parameter `topic` (mandatory) which specifies the essay topic.
   - Constructs a prompt (`prompt`) using the provided topic to generate an essay prompt with a length of 2000 words.
   - Utilizes the `generate` method of the `GoogleGenerativeAI` model to generate essay content based on the prompt.
   - Returns the generated essay content as the HTTP response.

5. **Server Execution**:
   - If the script is run directly (`__name__ == "__main__"`), it starts the FastAPI server using `uvicorn`, specifying `localhost` as the host and `8000` as the port.

### Usage:
To use the script:
- Ensure Python dependencies (`FastAPI`, `uvicorn`, `langchain`, `langchain_google_genai`, `dotenv`) are installed.
- Obtain a Google API key (`GOOGLE_API_KEY`) and store it in a `.env` file.
- Run the script using `uvicorn script_name:app --reload` in the terminal.
- Navigate to `http://localhost:8000/docs` to generate an essay on the specified topic.

This markdown document provides a clear overview of how the FastAPI server integrates with Google's Generative AI to dynamically generate essays based on user-provided topics, demonstrating its setup, usage, and key components.



## 🔗 Connect with Me

Feel free to connect with me on LinkedIn:

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://parthebhan143.wixsite.com/datainsights)

[![LinkedIn Profile](https://img.shields.io/badge/LinkedIn_Profile-000?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/parthebhan)

[![Kaggle Profile](https://img.shields.io/badge/Kaggle_Profile-000?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/parthebhan)

[![Tableau Profile](https://img.shields.io/badge/Tableau_Profile-000?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/parthebhan.pari/vizzes)


