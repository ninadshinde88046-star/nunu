import streamlit as st
st.title("some basic command like slider and button")
age=st.slider("Enter your age",1,100)
city=st.selectbox("Select your city",["delhi","mumbai","pune"])
if st.button("Submit"): 
    st.write("Your age is",age)
    st.write("Your city is",city)
