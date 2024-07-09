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


def generate_poem(topic, audience="child"):
    url = f"{BASE_URL}/poem"
    params = {'topic': topic, 'audience': audience}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['output']
    else:
        return {"error": f"Failed to generate poem. Status code: {response.status_code}"}

# Streamlit UI
st.title('Langchain AI Generator')

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

# Poem Generation Section
st.header('Generate Poem')
poem_topic = st.text_input('Enter a topic for the poem:')
poem_audience = st.selectbox('Select audience:', ['child', 'adult'])
if st.button('Generate Poem'):
    if poem_topic:
        poem_result = generate_poem(poem_topic, audience=poem_audience)
        if 'error' in poem_result:
            st.error(f"Error: {poem_result['error']}")
        else:
            st.success("Generated Poem:")
            st.write(poem_result)
    else:
        st.warning("Please enter a topic for the poem.")
