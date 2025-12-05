import streamlit as st
import pandas as pd

st.title("📈 Model Evaluation")

results = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest", "Gradient Boosting"],
    "MAE": [2.4379, 0.9176, 2.0854],
    "RMSE": [3.5975, 1.8400, 2.8884],
    "R2 Score": [0.8986, 0.9735, 0.9347]
})

st.write(results)

st.bar_chart(results.set_index("Model")[["MAE", "RMSE"]])
