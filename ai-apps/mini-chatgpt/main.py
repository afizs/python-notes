from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
import streamlit as st
import os

st.title("Mini-ChatGPT")

def generate_response(input_text):

    model = AzureAIChatCompletionsModel(
        endpoint = "https://models.github.ai/inference",
        model = "openai/gpt-4.1",
        credential = os.getenv("GITHUB_TOKEN"),
    )

    response = model.invoke(input_text)

    st.info(response.content)

with st.form("chat_interface"):
    text = st.text_area(
        "Enter text:"
    )
    submitted = st.form_submit_button("Submit")
    generate_response(text)
