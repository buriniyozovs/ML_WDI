# 📘 Life Expectancy Prediction Using Machine Learning  
### 6COSC017C-n — Machine Learning & Data Analytics Coursework Project

This project presents an end-to-end machine learning pipeline designed to **predict Life Expectancy** using socio-economic and demographic indicators from the **World Development Indicators (WDI)** dataset.

The solution includes:
- Full Exploratory Data Analysis (EDA)
- Data preprocessing & feature engineering
- Training of three ML models with hyperparameter tuning
- Model evaluation & comparison
- A deployed **Streamlit web application** for user-friendly predictions  

---

## 🚀 Project Overview

The purpose of this project is to develop a predictive model that estimates a country’s **Life Expectancy** based on factors such as GDP, school enrollment rates, labor force composition, and population structure.

The workflow consists of:

1. **Data Acquisition** – WDI dataset  
2. **EDA** – Understanding distributions, correlations, and missing values  
3. **Preprocessing** – Cleaning, encoding, scaling, feature selection  
4. **Model Training** – Linear Regression, Random Forest, Gradient Boosting  
5. **Model Evaluation** – MAE, RMSE, R²  
6. **Deployment** – Streamlit multi-page app  

---

## 📂 Project Structure
```
├── data/
│   └── wdi001.csv
│
├── models/
│   ├── life_exp_linear_regression.pkl
│   ├── life_exp_random_forest.pkl
│   └── life_exp_gradient_boosting.pkl
│
├── pages/
│   ├── 1_EDA.py
│   ├── 2_Preprocessing.py
│   ├── 3_Model_Training.py
│   ├── 4_Model_Evaluation.py
│   └── 5_Prediction_App.py
│
├── Home.py
├── requirements.txt
├── 16180.ipynb
└── README.md
```
---

## 📊 Dataset Description

- **Source**: World Development Indicators (WDI)
- **Rows**: 13,130  
- **Columns**: 25  
- **Coverage**: Global, all countries and regions, multiple decades  

Key features include:
- GDP Total, GDP Per Capita, GDP Growth Rate  
- School enrollment metrics (Primary, Secondary, Tertiary)  
- Labor force statistics  
- Population distribution  
- Life Expectancy (target variable)

---

## 🔍 Exploratory Data Analysis (EDA)

EDA covered the following:

### ✔ Dataset Structure
- 13,130 rows × 25 columns  
- Mix of numeric and categorical variables  

### ✔ Missing Value Analysis
- Literacy and enrollment indicators have high missingness  
- Life Expectancy missingness < 5% → suitable target  

### ✔ Descriptive Statistics
Included mean, median, std, min/max for all numeric features.

### ✔ Visual Insights
- Histograms for feature distribution  
- Boxplots for outlier detection  
- Correlation heatmap  

These steps helped reveal skewness, outliers, and relationships essential for model selection and preprocessing.

---

## 🛠 Data Preprocessing

Key steps performed:

### ✔ Dropped Non-Useful Columns
- ISO2 Code  
- Coordinates  
- Membership  
- Regional Group  

### ✔ Missing Value Handling
- Country-wise median imputation  
- Global median fallback  

### ✔ Feature Selection
Removed variables weakly correlated with Life Expectancy.

### ✔ Encoding & Scaling
- One-hot encoding for Country  
- StandardScaler for numeric features  

### ✔ Train-Test Split
- 80% training  
- 20% testing  

This ensures a clean dataset ready for ML models while preserving consistency during Streamlit predictions.

---

## 📈 Model Evaluation

Metrics used:

- **MAE** — Mean Absolute Error  
- **RMSE** — Root Mean Squared Error  
- **R² Score** — Goodness of fit  

Visualized using:
- Error comparison bar charts  
- Actual vs Predicted scatterplots  
- Residual distributions  

Gradient Boosting demonstrated the highest R² and lowest error values.

---

## 🌐 Streamlit Application

A multi-page application includes:

### ✔ Exploratory Data Analysis  
### ✔ Preprocessing Overview  
### ✔ Model Training Summary  
### ✔ Performance Evaluation  
### ✔ **Prediction Page**
- User selects **Country**
- Inputs key numeric indicators  
- Chooses **model** (LR, RF, GBM)  
- Receives real-time predicted Life Expectancy  
- Displays prediction summary & visualization  

**Deployed App:**  
https://itj8arqy4kru7uqfbuv9nx.streamlit.app/

---

## 💻 How to Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Streamlit app

```bash
streamlit run Home.py
```

---
