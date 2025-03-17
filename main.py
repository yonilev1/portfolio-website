import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

image_col, text_col = st.columns(2)

with image_col:
    st.image(r'C:\Users\yonil_n6n6nsl\PycharmProjects\personal_website\.venv\images\photo.png', width=400)
    st.write("If you scroll below, you will find some of the app I built Python, Feel free to contact me.")

with text_col:
    st.title("Yoni Leventhal")

    st.markdown("""
    <div style="background-color: #e8f4fd; padding: 15px; border-radius: 10px; text-align: justify;">
    Hey, I'm Yoni Leventhal, a 3rd-year Computer Science student at JCT and a passionate software engineer and creative problem solver.  
    Welcome to my portfolio, where I showcase the projects I've built and the technologies I love working with.  
    Feel free to explore — I'm sure you'll love it!
    </div>
    """, unsafe_allow_html=True)



thumbnail_col1,space_col, thumbnail_col2 = st.columns([1.5, 0.4, 1.5])

df = pd.read_csv(r".venv\data.csv", sep=";")
with thumbnail_col1:
    for index, row in df[:10].iterrows():
        st.write("")
        st.write("")
        st.write("")
        st.header(row["title"])
        st.write(row["description"])
        st.write(f"[Source code]({row["url"]})")
        st.image(row["image"])

with thumbnail_col2:
    for index, row in df[10:].iterrows():
        st.write("")
        st.write("")
        st.write("")
        st.header(row["title"])
        st.write(row["description"])
        st.write(f"[Source code]({row["url"]})")
        st.image(row["image"])


