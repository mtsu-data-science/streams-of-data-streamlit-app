import streamlit as st
from src.data_loader import read_data_from_s3
import plotly.express as px

st.title("Streams of Data Streamlit Example")

st.header("Data from S3")

s3_df = read_data_from_s3(f"s3://prod-streamlit-app-example-staged/iris-data/")

st.dataframe(s3_df)

st.header("Plotly Example")

df = px.data.tips()
fig = px.histogram(df, x="total_bill")

st.plotly_chart(fig, use_container_width=True)
