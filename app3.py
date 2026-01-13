import streamlit as st
st.title("make simple calculator")
num1=st.number_input("Enter first number")
num2=st.number_input("Enter second number")
operation=st.selectbox("choose operation",["add","subtract","multiply","divide"])
if st.button("Calculate"):
    if operation=="add":
        result=num1+num2
    elif operation=="subtract":
        result=num1-num2
    elif operation=="multiply":
        result=num1*num2
    elif operation=="divide":
        if num2!=0:
            result=num1/num2
        else:
            result="Error! Division by zero."
    st.write("The result is:",result)