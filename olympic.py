import streamlit as st
import pandas as pd
import pyodbc

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


    olypmic = pd.read_csv('olympic.csv') 
    st.write(olypmic.head())

    st.subheader('Distributions')

    st.bar_chart(olypmic)
    st.area_chart(olypmic)
    st.line_chart(olypmic)
    st.bar_chart(olypmic)

with features:
    st.header("The features we created")

with model_training:
    st.header("Time to train the model!")
    st.text("Here you get to choose the hyperparameters of the model and see how the performance changes.")