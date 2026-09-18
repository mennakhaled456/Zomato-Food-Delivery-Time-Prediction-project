# Zomato Food Delivery Time Prediction

A machine learning project that analyzes food delivery data and predicts the estimated delivery time for an order.

## 📌 Project Overview

Food delivery time can be affected by several factors such as traffic conditions, weather, distance, restaurant preparation time, and delivery-person characteristics.

The goal of this project is to analyze these factors, identify important patterns in the data, build regression models for delivery-time prediction, and deploy the final prediction model through an interactive Streamlit application.

## 🎯 Business Question

**What factors influence food delivery time, and can machine learning be used to predict the delivery time of a given order?**

## 📊 Dataset

The project uses a Zomato food delivery dataset containing approximately 45,500 orders.

The dataset includes information related to:

* Delivery person
* Restaurant
* Order and delivery times
* Weather conditions
* Traffic conditions
* Vehicle type
* Location coordinates
* Restaurant and delivery distances
* Delivery time

### Dataset Files

* `Zomato Dataset.csv` — Original dataset
* `Zomato_Cleaned_Dareen.csv` — Cleaned dataset used for analysis and modeling

## 🔄 Project Pipeline

The project follows the following workflow:

1. **Data Collection**
2. **Data Cleaning**

   * Missing-value handling
   * Duplicate removal
   * Outlier handling
   * Date/time processing
   * Geographic-coordinate validation
3. **Exploratory Data Analysis**

   * Distribution analysis
   * Correlation analysis
   * Categorical analysis
4. **Feature Engineering**

   * Distance-related features
   * Time-based features
   * Restaurant preparation time
   * Other relevant predictive features
5. **Machine Learning**

   * Linear Regression
   * Decision Tree
   * Random Forest
6. **Model Evaluation**
7. **Deployment**

   * Interactive Streamlit prediction application
8. **Dashboard**

   * Business and analytical insights using Power BI

## 🤖 Machine Learning

Several regression models were investigated and compared:

* Linear Regression — baseline model
* Decision Tree Regressor
* Random Forest Regressor

The trained Random Forest model is stored in:

`rf_delivery_time_model.pkl`

The complete data preparation, analysis, feature engineering, and modeling workflow is available in:

`notebooks/zomato_food_delivery.ipynb`

## 🖥️ Streamlit Application

The project includes an interactive Streamlit application that allows users to enter order-related information and receive a predicted delivery time.

Application file:

`app.py`

The deployed application link will be added here:

**Streamlit App:** *To be added*

## 📈 Dashboard

An interactive Power BI dashboard was developed to present the project's analytical findings and business insights.

The dashboard file will be added to:

`dashboard/`

**Dashboard / Published Link:** *To be added*

## 📁 Project Structure

```text
Zomato-Food-Delivery-Time-Prediction-project/
│
├── app.py
├── requirements.txt
├── rf_delivery_time_model.pkl
├── README.md
│
├── data/
│   ├── Zomato Dataset.csv
│   └── Zomato_Cleaned_Dareen.csv
│
├── notebooks/
│   └── zomato_food_delivery.ipynb
│
├── dashboard/
│   └── Power BI dashboard
│
├── report/
│   └── Project report
│
└── presentation/
    └── Project presentation
```

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook
* Streamlit
* Power BI
* Git & GitHub

## ▶️ Running the Streamlit Application

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
streamlit run app.py
```

## 📚 Project Documentation

The written project report will contain:

* Business question
* Dataset and data source
* Data preparation
* Exploratory data analysis
* Feature engineering
* Machine learning methodology
* Model evaluation
* Dashboard findings
* Limitations
* Conclusions

The report will be added to:

`report/`

## 👥 Team

This project was completed by a 5-member team.

Team member names and individual responsibilities will be added to this section.

## 🔗 Project Links

* **GitHub Repository:** https://github.com/mennakhaled456/Zomato-Food-Delivery-Time-Prediction-project
* **Streamlit Application:** To be added
* **Dashboard:** To be added

## 📖 Data Source

The original dataset source and access date will be documented here and in the final project report.

**Dataset URL:** To be added

**Access Date:** To be added

## ⚠️ Limitations

The model's predictions depend on the quality and characteristics of the available dataset. Factors that are not represented in the dataset may affect actual delivery times.

Further limitations and model-specific findings will be documented in the final project report.
