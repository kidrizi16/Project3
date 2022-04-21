import streamlit as st
import pandas as pd
import pyodbc
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

header = st.container()
dataset = st.container()

with header:
    st.title("Welcome to part 2")
    st.text("In this project we are going to analyze dependence between bolivar and US dollar")

with dataset:
    st.header("Dependence between bolivar and US dollar")
    st.text("This dataset was given to us by our instructor")
    data = pd.read_csv('co2.csv')
    st.write(data.head(50))

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list((range(1958,2019))))


@st.cache
def load_data(year):
    innerdf = pd.read_csv('co2.csv')
    return innerdf[innerdf.filter(['Date']).Date.str.endswith(f'{selected_year}') == True]


df_year = load_data(selected_year)

st.header('Display Stats of Selected Month')
st.write('Data Dimension: ' + str(df_year.shape[0]) + ' rows and ' + str(df_year.shape[1]) + ' columns.')
st.dataframe(df_year)
df_year_chart = df_year[["Date", "Average"]].rename(columns={'Date':'index'}).set_index('index')
st.line_chart(df_year_chart)