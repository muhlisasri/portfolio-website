import streamlit as st
from send_email import send_email

st.title("Contact Me")
with st.form(key="form"):
    user_email = st.text_input("Your Email : ")
    user_message = st.text_area("Your Message : ")
    message = f"""\
Subject: An email from {user_email}

from : {user_email}    
{user_message}  
"""
    submit = st.form_submit_button("Submit")
    if submit :
        send_email(message)
        st.info("Your message was send")