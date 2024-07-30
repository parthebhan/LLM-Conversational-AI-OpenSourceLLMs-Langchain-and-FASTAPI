# app_streamlit.py

import streamlit as st
import requests
import time

# Replace with the actual URL where your FastAPI server is running
BASE_URL = 'http://localhost:8000'

def generate_essay(topic):
    url = f"{BASE_URL}/essay_google"
    params = {'topic': topic}
    start_time = time.time()
    response = requests.get(url, params=params)
    end_time = time.time()
    response_time = end_time - start_time
    
    if response.status_code == 200:
        try:
            data = response.json()
            if 'generations' in data and data['generations']:
                essay_text = data['generations'][0][0]['text']
                return essay_text, response_time
        except KeyError:
            return {"error": "Unexpected response structure"}, response_time
    else:
        return {"error": f"Failed to generate essay. Status code: {response.status_code}"}, response_time

def generate_essay_groq(topic):
    url = f"{BASE_URL}/essay_groq"
    params = {'topic': topic}
    start_time = time.time()
    response = requests.get(url, params=params)
    end_time = time.time()
    response_time = end_time - start_time
    
    if response.status_code == 200:
        try:
            essay_content = response.json()
            return essay_content, response_time
        except KeyError:
            return {"error": "Unexpected response structure"}, response_time
    else:
        return {"error": f"Failed to generate essay using Groq. Status code: {response.status_code}"}, response_time

# Streamlit UI
st.title('Extending Conversational AI: Open Source LLMs, Langchain, and FastAPI')

# Essay Generation Section with Google Generative AI
st.header('Generate essay with Gemini')
essay_topic = st.text_input('')
if st.button('Gemini_Search'):
    if essay_topic:
        essay_result, response_time = generate_essay(essay_topic)
        if 'error' in essay_result:
            st.error(f"Error: {essay_result['error']}")
        else:
            st.success(f"Generated Essay (Response Time: {response_time:.4f} seconds):")
            st.write(essay_result)
    else:
        st.warning("Please enter your topic")

st.markdown('---')

# Essay Generation Section with Groq
st.header('Generate essay with Groq (Llama-3)')
essay_topic_groq = st.text_input(' ')
if st.button('Groq_Search'):
    if essay_topic_groq:
        essay_result_groq, response_time = generate_essay_groq(essay_topic_groq)
        if 'error' in essay_result_groq:
            st.error(f"Error: {essay_result_groq['error']}")
        else:
            st.success(f"Generated Essay (Response Time: {response_time:.4f} seconds):")
            st.write(essay_result_groq)
    else:
        st.warning("Please enter your topic")
