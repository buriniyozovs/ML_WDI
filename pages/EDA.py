import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Exploratory Data Analysis")

df = pd.read_csv("data/wdi001.csv")

# Dataset Preview
st.subheader("Dataset Preview")
st.write(df.head())

# Summary Statistics
st.subheader("Summary Statistics")
st.write(df.describe())

# Missing Values
st.subheader("Missing Values per Column")
st.write(df.isnull().sum())

# Correlation Matrix
st.subheader("Correlation Matrix (Numeric Columns)")

corr = df.select_dtypes(include=['float64', 'int64']).corr()

fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(corr, cmap="coolwarm")
st.pyplot(fig)

# Feature Distributions
st.subheader("Feature Distributions (Histograms)")

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
selected = list(numeric_cols[:5])
if 'Life Expectancy' in df.columns and 'Life Expectancy' not in selected:
    selected.append('Life Expectancy')

for col in selected:
    st.write(f"### Distribution of {col}")
    fig, ax = plt.subplots()
    sns.histplot(df[col].dropna(), kde=True)
    st.pyplot(fig)
