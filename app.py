from fastapi import FastAPI,Query
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from groq import Groq
import uvicorn
import os

from dotenv import load_dotenv
import json


# Load environment variables from .env file
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Groq client with API key from environment variables
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Create FastAPI application instance
app=FastAPI(
    title="Langchain Server",
    version="1.1",
    decsription="A simple API Server"
)

# Initialize Google Generative AI model instance
model_google  = GoogleGenerativeAI(model="gemini-1.5-pro-latest", google_api_key=google_api_key)


# Define API endpoint to enerate responses using Google's Generative AI
@app.get("/chat_google")
async def essay_prompt(topic: str = Query(..., description="Topic for the essay")):
    # Generate essay using GoogleGenerativeAI model
    prompt = f"Write me an essay about {topic} with 2000 words."
    essay_content = model_google.generate(prompts=[prompt], max_tokens=100)
    return essay_content

# Define API endpoint to generate responses using Groq
@app.get("/chat_groq")
async def essay_prompt_groq(topic: str = Query(..., description="Topic for the essay")):
    chat_completion = client.chat.completions.create(messages=[{"role": "user","content": topic,}],model="llama3-8b-8192",)
    return chat_completion.choices[0].message.content

# Run the FastAPI application using uvicorn server
if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)