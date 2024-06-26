import streamlit as st
import pandas
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    try:
        st.image("images/photo.png")
    except FileNotFoundError:
        st.error("Image file not found. Please check the file path.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

with col2:
    st.title("Saklain Nizam thakur")
    content = """ 
I am Saklain Nizam Thakur, a Python developer. I graduated in 2024 and have been passionate about coding and problem-solving. Feel free to reach out if you have any questions or need assistance!"""
    st.info(content)
st.markdown("""
Below you can find some of the apps that I have build in python recently. Feel  free to contact me!""")


col3, empty_col,  col4 = st.columns([1.5, 0.5, 1.5 ])
df = pandas.read_csv("data.csv", sep = ";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image ("images/"+row["image"])
        st.write(f"[source code ]({row['url']})")
with col4 :
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image ("images/"+row["image"])
        st.write(f"[source code ]({row['url']})")





