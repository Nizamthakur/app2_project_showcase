import streamlit as st
st.header("contact us")
with  st.form(key ="user_email"):
    user_email = st.text_input("Your Email Address")
    massage = st.text_area("Your massage Here")
    button = st.form_submit_button ("submit")

    if button :
        massage = massage + user_email
        