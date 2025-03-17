import streamlit as st
import emoji as em
import re
import email_sender as es


st.header('Contact Me' + em.emojize(":slightly_smiling_face:"))

with st.form(key="user's form", clear_on_submit=True):
    username = st.text_input("Enter your name:")
    users_email_address = st.text_input("Enter you gmail address:")
    users_massage = st.text_area("Enter you you massage and I will get back to you" + em.emojize(":heart:"),height=200, max_chars=200)
    user_submit_button = st.form_submit_button('Submit')

    if user_submit_button:
        pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
        if re.match(pattern, users_email_address):
            es.send_email(users_email_address, username)
            st.success("Your message has been sent successfully!")
        else:
            st.error("Please enter a valid Gmail address.")
