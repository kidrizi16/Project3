import streamlit as st
import pandas as pd
import pyodbc
import numpy as np

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Welcome part 2")
    st.text("In this project we are going to analyze number of medals")

with dataset:
    st.header("Number of medals")
    st.text("This dataset was given to us by our instructor")

    df = pd.read_csv('olympic.csv')[["NOC", "Medal"]]
    df['Gold'] = np.where(df['Medal'] == 'Gold', 1, 0)
    df['Silver'] = np.where(df['Medal'] == 'Silver', 1, 0)
    df['Bronze'] = np.where(df['Medal'] == 'Bronze', 1, 0)
    df2 = df.groupby(['NOC']).sum()[["Gold", "Silver", "Bronze"]]
    olypmic=df2.query('Gold + Silver + Bronze >= 500')

    st.write(olypmic.head())

    st.subheader('Distributions')

    st.bar_chart(olypmic)
