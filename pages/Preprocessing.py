import streamlit as st

st.title("⚙️ Data Preprocessing Steps")

st.markdown("""
### ✔ Handling Missing Values  
- Country-specific median imputation  
- Global median for fallback

### ✔ Encoding  
- Membership → binary  
- One-hot encoding for categorical columns  

### ✔ Feature Engineering  
- Latitude & Longitude from Coordinates  
- Removing high-missing columns  

### ✔ Scaling  
- StandardScaler applied to numeric features  

### ✔ Train/Validation/Test Split  
- 70% / 15% / 15%
""")
