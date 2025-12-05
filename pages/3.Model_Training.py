import streamlit as st

st.title("🤖 Model Training Summary")

st.markdown("""
### ✔ Trained Machine Learning Models  
The following regression models were trained for predicting **Life Expectancy**:

- **Linear Regression**  
  - Basic linear model  
  - Hyperparameter tuning applied (fit_intercept, positive)

- **Random Forest Regressor**  
  - Non-linear ensemble model  
  - Grid Search used to tune parameters  
    (n_estimators, max_depth, min_samples_split, min_samples_leaf)

- **Gradient Boosting Regressor**  
  - Boosted decision tree model  
  - Grid Search used to optimize  
    (learning_rate, n_estimators, max_depth, subsample)

---

### ✔ Training Details  
- Training performed on the **70% training split**  
- Final performance evaluated on the **30% test split**  
- Scaling and preprocessing applied before model fitting  
- Models were optimized using cross-validation during Grid Search

---

### ✔ Saved Models  
Trained models have been saved in the `models/` directory for use in the prediction interface.
""")
