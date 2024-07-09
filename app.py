from fastapi import FastAPI,Query
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
import uvicorn
import os

from dotenv import load_dotenv
import json

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"
)

# Example model or handler for Google Gemini
model  = GoogleGenerativeAI(model="gemini-1.5-pro-latest", google_api_key=google_api_key)

# Route for essay prompt with Gemini model
@app.get("/essay")
async def essay_prompt(topic: str = Query(..., description="Topic for the essay")):
    # Generate essay using GoogleGenerativeAI model
    prompt = f"Write me an essay about {topic} with 2000 words."
    essay_content = model.generate(prompts=[prompt], max_tokens=100)
    return essay_content


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)