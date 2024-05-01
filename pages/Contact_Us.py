import streamlit as st
from send_email import send_email
st.header("contact us")
with st.form(key ="user_email"):
    user_email = st.text_input("Your Email Address")
    raw_massage = st.text_area("Your massage Here")
    subject = f"New email from {user_email}"
    message = f"""\
            Subject: {subject}\n
            From: {user_email}\n
            {raw_massage}
            """
    button = st.form_submit_button("submit")
    print(button)
    if button:
        send_email(message)
        st.info("your email was sent sucesfully ")
        # massage = massage + user_email
