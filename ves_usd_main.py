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


    campaign_data = pd.read_csv('ves-usd.csv')
    st.write(campaign_data.head())

    st.subheader('Several distributions')
    campaign_data_by_Region = campaign_data.groupby(['Region']).sum()[["Revenue", "Revenue_Target"]]
    campaign_data_by_Country = campaign_data.groupby(['Country']).sum()[["Revenue", "Revenue_Target"]]
    campaign_data_by_Product_Category = campaign_data.groupby(['Product_Category']).sum()[["Revenue", "Revenue_Target"]]
    campaign_data_by_Campaign_Name = campaign_data.groupby(['Campaign_Name']).sum()[["Revenue", "Revenue_Target"]]
    st.bar_chart(campaign_data_by_Region)
    st.area_chart(campaign_data_by_Country)
    st.line_chart(campaign_data_by_Product_Category)
    st.bar_chart(campaign_data_by_Campaign_Name)


with features:
    st.header("The features we created")

with model_training:
    st.header("Time to train the model!")
    st.text("Here you get to choose the hyperparameters of the model and see how the performance changes.")