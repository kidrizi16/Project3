import streamlit as st
import pandas as pd

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()

with header:
    st.title("Welcome to project no 3 of team no 5")
    st.text("In this project we are going to analyze campaigns")

with dataset:
    st.header("Campaign analytics dataset")
    st.text("This dataset was given to us by our instructor")

    campaign_data = pd.read_csv('C:/Users/U761133/Desktop/Project3/campaignanalytics2.csv')
    st.write(campaign_data.head())

    st.subheader('Pick up revenue distribution')
    our_data = pd.DataFrame(campaign_data['Revenue'].value_counts()).head(50)
    st.bar_chart(our_data)

with features:
    st.header("The features we created")

with model_training:
    st.header("Time to train the model!")
    st.text("Here you get to choose the hyperparameters of the model and see how the performance changes.")