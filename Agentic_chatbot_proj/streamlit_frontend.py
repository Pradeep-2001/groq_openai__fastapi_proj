import streamlit as st
import requests

st.set_page_config(page_title="AI Agent")
st.title("AI Chatbot")
st.write("create and interact with AI agents")

system_prompt= st.text_area("Define you AI Agents")


MODEL_NAMES_GROQ=["llama-3.3-70b-versatile"]

provider=st.radio("Select Provider",("Groq"))

if provider == "Groq":
    selected_model= st.selectbox("Select Groq Model",MODEL_NAMES_GROQ)

allow_web_search= st.checkbox("Allow web search")

user_query= st.text_area("Enter your query")

API_URL= "http://localhost:9999/chat"

if(st.button("Ask Agent")):
    if user_query.strip():

        payload={
            "model_name":selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages":[user_query],
            "allow_search": allow_web_search
        }

        response= requests.post(API_URL,json=payload)
        if response.status_code== 200:
            response_data= response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"Final Response: {response_data}")





