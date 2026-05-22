import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Sales Data Dashboard")

df = pd.read_csv("data.csv")

st.write("### Dataset Preview")
st.dataframe(df.head())

category_sales = df.groupby("Category")["Sales"].sum()

st.write("### Sales by Category")
st.bar_chart(category_sales)

st.write("### Insights")
st.write("Highest Sales Category:", category_sales.idxmax())