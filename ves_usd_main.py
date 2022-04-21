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


    rate = pd.read_csv('ves-usd.csv')[["Date", "Rate"]].rename(columns={'Date':'index'}).set_index('index')
    st.write(rate.head(50))

    st.subheader('Distributions')

    st.line_chart(rate)

st.sidebar.header('User Input Features')
selected_month = st.sidebar.selectbox('Month', list((range(3,10))))

@st.cache
def load_data(month):
    innerdf = pd.read_csv('ves-usd.csv')
    return innerdf[innerdf.filter(['Date']).Date.str.startswith(f'{selected_month}')==True]


df_month = load_data(selected_month)

st.header('Display Stats of Selected Month')
st.write('Data Dimension: ' + str(df_month.shape[0]) + ' rows and ' + str(df_month.shape[1]) + ' columns.')
st.dataframe(df_month)
df_month_chart = df_month[["Date", "Rate"]].rename(columns={'Date':'index'}).set_index('index')
st.line_chart(df_month_chart)


