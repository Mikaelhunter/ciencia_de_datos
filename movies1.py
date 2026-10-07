import streamlit as st
import pandas as pd

DATA_URL = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/nosql/refs/heads/main/csv/movies.csv", encoding='latin1')
st.dataframe(DATA_URL)

sidebar = st.sidebar
sidebar.title("Funciones de filtrado")
sidebar.write("Aquí van los elementos de entrada.")