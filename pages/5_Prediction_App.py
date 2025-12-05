import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.title("🔮 Life Expectancy Prediction App")

st.markdown("""
Use this app to predict **Life Expectancy** using different ML models.
Select a model, enter input values, and view predictions + comparison graphs.
""")

# LOAD MODELS
models = {
    "Linear Regression": joblib.load("models/life_exp_linear_regression.pkl"),
    "Random Forest": joblib.load("models/life_exp_random_forest.pkl"),
    "Gradient Boosting": joblib.load("models/life_exp_gradient_boosting.pkl")
}

# LOAD DATASET TO EXTRACT COUNTRIES
df = pd.read_csv("data/wdi001.csv", thousands=",")
country_list = sorted(df["Country"].dropna().unique().tolist())

# USER INPUTS
st.subheader("📥 Input Features")

selected_model_name = st.selectbox(
    "🤖 Select Model for Prediction",
    list(models.keys())
)

country = st.selectbox("🌍 Country", country_list)

year = st.number_input("📅 Year", min_value=1960, max_value=2025, value=2020)

gdp_total = st.number_input("💰 GDP Total", min_value=0.0, value=5_000_000_000.0)
gdp_per_capita = st.number_input("💵 GDP Per Capita", min_value=0.0, value=20000.0)

primary = st.number_input("📘 Primary School Enrollment (%)", min_value=0.0, value=95.0)
secondary = st.number_input("📗 Secondary School Enrollment (%)", min_value=0.0, value=80.0)
tertiary = st.number_input("📙 Tertiary School Enrollment (%)", min_value=0.0, value=40.0)

# Build input DF
input_df = pd.DataFrame({
    "Year": [year],
    "GDP Total": [gdp_total],
    "GDP Per Capita": [gdp_per_capita],
    "Primary School Enrollment": [primary],
    "Secondary School Enrollment": [secondary],
    "Tertiary School Enrollment": [tertiary],
    "Country": [country]
})

# PREDICTION
if st.button("Predict Life Expectancy"):
    
    selected_model = models[selected_model_name]

    prediction = float(selected_model.predict(input_df)[0])   # FIXED

    st.success(f"🎯 **Predicted Life Expectancy:** {prediction:.2f} years")
    st.write("Input Summary:")
    st.dataframe(input_df)

    # VISUALIZATION — Compare Model Predictions
    st.subheader("📊 Model Comparison Chart")

    comp_data = []
    for name, mdl in models.items():
        comp_data.append({
            "Model": name,
            "Prediction": float(mdl.predict(input_df)[0])   # FIXED
        })

    comp_df = pd.DataFrame(comp_data)

    st.bar_chart(comp_df.set_index("Model"))

    # VISUALIZATION — Prediction Trend for Country
    st.subheader(f"📈 Life Expectancy Trend for {country}")

    country_hist = df[df["Country"] == country][["Year", "Life Expectancy"]].dropna()

    if len(country_hist) > 0:
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(country_hist["Year"], country_hist["Life Expectancy"], marker='o', label="Actual History")
        ax.axhline(prediction, color="red", linestyle="--", label="Predicted Value")
        ax.set_title(f"Life Expectancy Trend — {country}")
        ax.set_xlabel("Year")
        ax.set_ylabel("Life Expectancy")
        ax.legend()
        st.pyplot(fig)
    else:
        st.info("No historical life expectancy data available for this country.")
