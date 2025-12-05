import streamlit as st
import pandas as pd
import joblib

st.title("🔮 Life Expectancy Prediction App")

st.markdown("""
Enter the required features below to predict **Life Expectancy** for a selected country.
The model automatically handles scaling and encoding.
""")

# LOAD MODEL
model = joblib.load("models/life_exp_random_forest.pkl")

# LOAD DATASET TO EXTRACT COUNTRIES
df = pd.read_csv("data/wdi001.csv", thousands=",")

country_list = sorted(df["Country"].dropna().unique().tolist())

# INPUT FORM
st.subheader("📥 Input Features")

country = st.selectbox("🌍 Country", country_list)

year = st.number_input("📅 Year", min_value=1960, max_value=2025, value=2020)

gdp_total = st.number_input("💰 GDP Total", min_value=0.0, value=5000000000.0)
gdp_per_capita = st.number_input("💵 GDP Per Capita", min_value=0.0, value=20000.0)

primary = st.number_input("📘 Primary School Enrollment (%)", min_value=0.0, value=95.0)
secondary = st.number_input("📗 Secondary School Enrollment (%)", min_value=0.0, value=80.0)
tertiary = st.number_input("📙 Tertiary School Enrollment (%)", min_value=0.0, value=40.0)

# PREDICTION
if st.button("Predict Life Expectancy"):
    input_df = pd.DataFrame({
        "Year": [year],
        "GDP Total": [gdp_total],
        "GDP Per Capita": [gdp_per_capita],
        "Primary School Enrollment": [primary],
        "Secondary School Enrollment": [secondary],
        "Tertiary School Enrollment": [tertiary],
        "Country": [country]
    })

    prediction = model.predict(input_df)[0]

    st.success(f"🎯 Predicted Life Expectancy: **{prediction:.2f} years**")

    st.write("Input preview:")
    st.dataframe(input_df)
