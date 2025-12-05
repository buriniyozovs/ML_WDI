import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Exploratory Data Analysis")

df = pd.read_csv("data/dataset.csv")

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Missing Values")
st.write(df.isnull().sum())

st.subheader("Correlation Matrix")
corr = df.select_dtypes(include=['float64', 'int64']).corr()

fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(corr, cmap="coolwarm")
st.pyplot(fig)
