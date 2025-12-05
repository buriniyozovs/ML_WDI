import streamlit as st
import pandas as pd
import joblib

st.title("🔮 Predict Life Expectancy")

# Load model
model = joblib.load("models/best_random_forest.pkl")

st.write("Enter feature values:")

# === User Inputs ===
year = st.number_input("Year", min_value=1900, max_value=2100, step=1)
gdp_total = st.number_input("GDP Total", min_value=0.0)
gdp_capita = st.number_input("GDP Per Capita", min_value=0.0)
primary_school = st.number_input("Primary School Enrollment", min_value=0.0)
secondary_school = st.number_input("Secondary School Enrollment", min_value=0.0)
tertiary_school = st.number_input("Tertiary School Enrollment", min_value=0.0)

# Create input DataFrame
input_df = pd.DataFrame({
    "Year": [year],
    "GDP Total": [gdp_total],
    "GDP Per Capita": [gdp_capita],
    "Primary School Enrollment": [primary_school],
    "Secondary School Enrollment": [secondary_school],
    "Tertiary School Enrollment": [tertiary_school]
})

st.subheader("📄 Input Summary")
st.write(input_df)

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"🎯 Predicted Life Expectancy: **{prediction:.2f} years**")
