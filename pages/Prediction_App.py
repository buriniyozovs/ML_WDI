import streamlit as st
import pandas as pd
import joblib

st.title("🔮 Predict Life Expectancy")

model = joblib.load("models/best_random_forest.pkl")

st.write("Enter feature values:")

gdp = st.number_input("GDP Total", min_value=0.0)
population = st.number_input("Population Total", min_value=0.0)
gdp_capita = st.number_input("GDP Per Capita", min_value=0.0)
school_sec = st.number_input("Secondary School Enrollment", min_value=0.0)

input_df = pd.DataFrame({
    "GDP Total": [gdp],
    "Population Total": [population],
    "GDP Per Capita": [gdp_capita],
    "Secondary School Enrollment": [school_sec]
})

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Life Expectancy: {prediction:.2f} years")
