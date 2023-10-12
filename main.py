import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1 :
    st.image('images/muhlisasri.jpg')

with col2 :
    st.title('Muhlis M Asri, S.Si.')
    content = """
    Menyelesaikan pendidikan di Universitas Hasanuddin Program Studi Statistika pada tahun 2015.
    """
    st.write(content)

