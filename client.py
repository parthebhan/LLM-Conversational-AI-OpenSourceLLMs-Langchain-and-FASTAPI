import streamlit as st
import requests

# Replace with the actual URL where your FastAPI server is running
BASE_URL = 'http://localhost:8000'

def generate_essay(topic):
    url = f"{BASE_URL}/essay"
    params = {'topic': topic}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            if 'generations' in data and data['generations']:
                essay_text = data['generations'][0][0]['text']
                return essay_text
        except KeyError:
            return {"error": "Unexpected response structure"}
    else:
        return {"error": f"Failed to generate essay. Status code: {response.status_code}"}

# Streamlit UI
st.title('FastAPI Server with Google Generative AI Integration using Langchain')

# Essay Generation Section
st.header('Generate Essay')
essay_topic = st.text_input('Enter a topic for the essay:')
if st.button('Generate Essay'):
    if essay_topic:
        essay_result = generate_essay(essay_topic)
        if 'error' in essay_result:
            st.error(f"Error: {essay_result['error']}")
        else:
            st.success("Generated Essay:")
            st.write(essay_result)
    else:
        st.warning("Please enter a topic for the essay.")

st.markdown('---')


