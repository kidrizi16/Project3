import streamlit as st
import pandas as pd
import pyodbc
import numpy as np
import plotly.express as px

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

df = pd.read_csv('olympic.csv')[["ID", "Height", "Weight", "Medal"]]
df1 = df[df[["ID", "Height", "Weight", "Medal"]].notnull().all(1)].groupby(["ID", "Height", "Weight"]).count().query('Medal > 5')
df1_final = df1.groupby(["Height", "Weight"]).sum("Medal")
df1_final = df1_final.reset_index()
fig = px.scatter(df1_final, x="Height", y="Weight", size ="Medal", log_x=True, size_max=60)
fig.show()

"""
original = pd.read_csv('olympic.csv')
# Extract count of medals per country per year
df2 = original.groupby(['Name', 'Medal']).count()  # Group data and count medals by type
df2 = df2.reset_index()
df2 = df2.iloc[:, 4:6]  # Selected needed columns and drop excess
df2 = df2.rename(columns={'Name': 'Medal'})

# Combine all information: gdp and medal count
final_df = pd.merge(medals_df, df3, left_on=['country_name', 'year'], right_on=['country_name', 'year'])
"""