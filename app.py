from fastapi import FastAPI,Query
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from langchain_google_genai import GoogleGenerativeAI
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

##ollama llama2
llm=Ollama(model="llama2")

# Route for essay prompt with Gemini model
@app.get("/essay")
async def essay_prompt(topic: str = Query(..., description="Topic for the essay")):
    # Generate essay using GoogleGenerativeAI model
    prompt = f"Write me an essay about {topic} with 2000 words."
    essay_content = model.generate(prompts=[prompt], max_tokens=100)
    return essay_content

# Route for poem prompt with Ollama model
@app.get("/poem")
async def poem_prompt(topic: str = Query(..., description="Topic for the poem"),
                      audience: str = Query("child", description="Audience type ('child' or 'adult')")):
    # Generate poem using Ollama model
    prompt = f"Write me a poem about {topic} for a {audience} with 100 words."
    poem_content = llm.generate(prompt=prompt, topic=topic, audience=audience, max_tokens=100)
    return {"poem": poem_content}

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)