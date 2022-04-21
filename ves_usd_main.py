import streamlit as st
import pandas as pd
import pyodbc

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Welcome part 2")
    st.text("In this project we are going to analyze dependence between bolivar and US dollar")

with dataset:
    st.header("Dependence between bolivar and US dollar")
    st.text("This dataset was given to us by our instructor")


    rate = pd.read_csv('ves-usd.csv')[["Date", "Rate"]].rename(columns={'Date':'index'}).set_index('index')
    st.write(rate.head())

    st.subheader('Distributions')

    st.line_chart(rate)


with features:
    st.header("The features we created")

with model_training:
    st.header("Time to train the model!")
    st.text("Here you get to choose the hyperparameters of the model and see how the performance changes.")