import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title='Muhlis M Asri, S.Si. Programmer Portfolio',
        page_icon="👨‍💻")
col1, col2 = st.columns(2)

with col1 :
    st.image('images/muhlisasri.jpg')

with col2 :
    st.title('Muhlis M Asri, S.Si.')
    content = """
    Menyelesaikan pendidikan di Universitas Hasanuddin Program Studi Statistika pada tahun 2015.
    """
    st.write(content)

col3, col4 = st.columns(2)
df = pd.read_csv("data.csv", sep=";")

with col3 :
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4 :
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")