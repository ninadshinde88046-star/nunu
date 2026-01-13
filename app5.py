import streamlit as st
import google.generativeai as genai
st.title("welcome to streamlit with generative ai")
 
user_input=st.text_input("ask me anything")
genai.configure(api_key="AIzaSyAKY4w4CYmLlSxWFTUa4jEI4gh061fgyZY")
model=genai.GenerativeModel("models/gemini-2.5-flash")
if user_input:
 response=model.generate_content(user_input)
st.write("response:", response.text)