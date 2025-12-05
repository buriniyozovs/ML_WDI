import streamlit as st

st.title("⚙️ Data Preprocessing Steps")

st.markdown("""
### ✔ Handling Missing Values  
- Country-specific median imputation for numeric features  
- Global median imputation for countries with only one record  
- Dropping columns with extremely high missing percentages (80%+)

---

### ✔ Encoding  
- *Membership* converted to binary (Member → 1, Non-member → 0)  
- One-hot encoding applied to categorical features (e.g., Country, Regional Group)

---

### ✔ Feature Engineering  
- Removed the original *Coordinates*, *ISO2 Code* and *Membership* columns  
- Removed non-informative or weakly correlated features when needed

---

### ✔ Scaling  
- StandardScaler applied to all numeric features  
- Ensures models (e.g., Linear Regression, Gradient Boosting) train effectively

---

### ✔ Dataset Split  
- Split into **Training (70%)** and **Test (30%)**  
- Test set used for final evaluation and comparison of models
""")
