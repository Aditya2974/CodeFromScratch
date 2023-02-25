import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="FIRST PAGE", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.json()

lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_vnikrcia.json")


with st.container():
    st.subheader("Hi I am Aditya Deshpande")
    st.title("A data anaylst from Germany")
    st.write("I am passionate about finding ways about coding")
    st.write("[Learn More ](https://youtu.be/F4tvM4Vb3A0)")

# Lottie Files are json based animation files!

with st.container():
    st.write("-------")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("----------")
        st.write("######")
        st.write("[Youtube](https://youtu.be/F4tvM4Vb3A0)")

    with right_column:
        st_lottie(lottie_coding)
