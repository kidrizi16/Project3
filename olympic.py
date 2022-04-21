import streamlit as st
import pandas as pd
import pyodbc
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

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

original = pd.read_csv('olympic.csv')
df6 = original[original[["Age", "Height", "Weight", "Sport"]].notnull().all(1)]
df6 = df6[df6["Sport"] == 'Judo']
df6_2 = df6[["Age", "Height", "Weight"]]

fig2 = sns.boxplot(x="Age", data=df6_2, palette="Set3")
fig2.figure

fig3 = sns.violinplot(x="Height", data=df6_2, palette="Set3")
fig3.figure

fig4 = sns.swarmplot(x="Weight", data=df6_2, palette="Set3")
fig4.figure
