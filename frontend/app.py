import streamlit as st
import requests

def upload_resume():
    uploaded_file = st.file_uploader("Upload Your Resume", type=["txt", "pdf"])
    if uploaded_file is not None:
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8000/upload_resume/", files=files)
        st.json(response.json())

st.title("Skill Gap Analysis Tool")
upload_resume()