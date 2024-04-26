import streamlit as st
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    try:
        st.image("images/photo.png", width=600 )
    except FileNotFoundError:
        st.error("Image file not found. Please check the file path.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

with col2:
    st.title("Saklain Nizam thakur")
    content = """ Hi, I am saklain nizam thakur. I work as a Python developer. I graduated in 2024"""
    st.info(content)
