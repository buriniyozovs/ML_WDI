import streamlit as st

st.title("🤖 Model Training Summary")

st.markdown("""
### Trained Models  
- Linear Regression (Hyperparameter tuned)  
- Random Forest Regressor (Grid Search)  
- Gradient Boosting Regressor (Grid Search)  

Models trained using **train** and **validation** sets.

All models saved in the `models/` folder.
""")
