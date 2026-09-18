# 🍔 Zomato Food Delivery Time Prediction

A machine learning project that analyzes food delivery data, identifies factors affecting delivery time, and predicts the estimated delivery time for new orders.

The project includes data cleaning, exploratory data analysis, feature engineering, regression modeling, an interactive Streamlit prediction application, and a Power BI dashboard.

---

## 📌 Project Overview

Food delivery time can be influenced by several factors, including:

* Traffic conditions
* Weather
* Delivery distance
* Restaurant preparation time
* Delivery-person characteristics
* Vehicle condition
* Multiple deliveries
* Order timing
* Festival days
* City type

The goal of this project is to analyze these factors, build machine learning models that predict delivery time, and deploy the final prediction model through an interactive web application.

---

## 🎯 Business Question

**What factors influence food delivery time, and can machine learning be used to predict the delivery time of a given order?**

---

## 📊 Dataset

The project uses a Zomato food delivery dataset containing approximately **45,500 orders**.

The dataset contains information related to:

* Delivery person
* Restaurant
* Order and delivery times
* Weather conditions
* Traffic conditions
* Vehicle type and condition
* Location coordinates
* Multiple deliveries
* Festival information
* Delivery time

### Dataset Files

| File                             | Description                                    |
| -------------------------------- | ---------------------------------------------- |
| `data/Zomato Dataset.csv`        | Original dataset                               |
| `data/Zomato_Cleaned_Dareen.csv` | Cleaned dataset used for analysis and modeling |

---

## 🔄 Project Workflow

The project follows an end-to-end data science and machine learning workflow:

### 1. Data Collection

The original food delivery dataset was collected and prepared for analysis.

### 2. Data Cleaning

The data preparation process included:

* Handling missing values
* Removing duplicates
* Handling outliers
* Processing date and time information
* Validating geographic information
* Preparing categorical and numerical features

### 3. Exploratory Data Analysis

The dataset was explored using:

* Distribution analysis
* Correlation analysis
* Categorical analysis
* Numerical summaries
* Visualization

### 4. Feature Engineering

Additional predictive features were created, including:

* Delivery distance
* Order hour
* Day of week
* Weekend indicator
* Rush-hour indicator
* Restaurant preparation time
* Other order and delivery characteristics

### 5. Machine Learning

Three regression approaches were investigated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

### 6. Model Evaluation

The regression models were evaluated and compared using appropriate regression metrics.

The trained Random Forest model was selected for the deployed prediction application.

### 7. Deployment

The trained model was integrated into an interactive **Streamlit** application that allows users to enter order conditions and receive an estimated delivery time.

### 8. Dashboard

A Power BI dashboard is included as part of the project to communicate analytical findings and business insights.

---

## 🤖 Machine Learning Model

The project investigates several regression models:

| Model                   | Role                        |
| ----------------------- | --------------------------- |
| Linear Regression       | Baseline model              |
| Decision Tree Regressor | Non-linear regression model |
| Random Forest Regressor | Final deployed model        |

The trained Random Forest model is stored in:

```text
rf_delivery_time_model.pkl
```

The complete data preparation, analysis, feature engineering, and modeling workflow is available in:

```text
notebooks/zomato_food_delivery.ipynb
```

---

## 🖥️ Streamlit Application

The project includes an interactive Streamlit application for delivery-time prediction.

Users can provide information such as:

* Delivery-person age
* Delivery-person rating
* Vehicle condition
* Order date and time
* Multiple deliveries
* Order type
* Vehicle type
* Preparation time
* Delivery distance
* Weather
* Traffic
* Festival status
* City type

The application then uses the trained Random Forest model to estimate the delivery time.

### 🚀 Live Application

**[Open the Streamlit App](https://zomato-food-delivery-time-prediction-project-hu6scvwmeu88brhbc.streamlit.app/)**

### Application Files

```text
app.py
rf_delivery_time_model.pkl
requirements.txt
```

---

## 📈 Power BI Dashboard

An interactive Power BI dashboard is part of the project and presents:

* Delivery-time analysis
* Business insights
* Data distributions
* Relevant relationships and patterns
* Interactive visualizations

The dashboard file will be added to:

```text
dashboard/
```

**Dashboard:** To be added when the final dashboard file is received.

---

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
│   └── Final Power BI dashboard
│
├── report/
│   └── Final project report
│
└── presentation/
    └── Final project presentation
```

---

## 🛠️ Technologies Used

### Programming & Data Analysis

* Python
* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn
* Power BI

### Machine Learning

* Scikit-learn
* Random Forest
* Decision Tree
* Linear Regression

### Development & Deployment

* Jupyter Notebook
* Streamlit
* Git
* GitHub

---

## ▶️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/mennakhaled456/Zomato-Food-Delivery-Time-Prediction-project.git
```

### 2. Enter the project directory

```bash
cd Zomato-Food-Delivery-Time-Prediction-project
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will then open in your browser.

---

## 📓 Notebook

The complete machine learning workflow is available in:

```text
notebooks/zomato_food_delivery.ipynb
```

The notebook includes the project's data preparation, exploratory analysis, feature engineering, model training, and evaluation workflow.

---

## 📚 Project Documentation

The final written documentation will cover:

* Business question
* Dataset and data source
* Data preparation
* Exploratory data analysis
* Feature engineering
* Machine learning methodology
* Model evaluation
* Key findings
* Dashboard insights
* Limitations
* Conclusion
* Project links

The final report will be added to:

```text
report/
```

---

## 👥 Team

This project was completed by a **5-member team**.

Team member names and individual responsibilities will be added to the final project documentation.

---

## 🔗 Project Links

| Resource                   | Link                                                                                              |
| -------------------------- | ------------------------------------------------------------------------------------------------- |
| GitHub Repository          | [GitHub](https://github.com/mennakhaled456/Zomato-Food-Delivery-Time-Prediction-project)          |
| Live Streamlit Application | [Open App](https://zomato-food-delivery-time-prediction-project-hu6scvwmeu88brhbc.streamlit.app/) |
| Power BI Dashboard         | To be added                                                                                       |
| Project Report             | To be added                                                                                       |
| Presentation               | To be added                                                                                       |

---

## 📖 Data Source

The dataset source and access information will be documented in the final project report.

**Dataset URL:** To be added

**Access Date:** To be added

---

## ⚠️ Limitations

Machine learning predictions depend on the quality and characteristics of the available training data.

Actual delivery times may also be affected by factors that are not represented in the dataset, such as unexpected traffic events, operational issues, restaurant delays, weather changes, and other real-world conditions.

---

## 📄 Project Status

| Component                 | Status        |
| ------------------------- | ------------- |
| Data Collection           | ✅ Complete    |
| Data Cleaning             | ✅ Complete    |
| Exploratory Data Analysis | ✅ Complete    |
| Feature Engineering       | ✅ Complete    |
| Machine Learning          | ✅ Complete    |
| Model Deployment          | ✅ Complete    |
| Streamlit Application     | ✅ Live        |
| Power BI Dashboard        | ⏳ To be added |
| Written Report            | ⏳ To be added |
| Presentation              | ⏳ To be added |

---

## ⭐ Project Links

**GitHub:**
https://github.com/mennakhaled456/Zomato-Food-Delivery-Time-Prediction-project

**Live Streamlit Application:**
https://zomato-food-delivery-time-prediction-project-hu6scvwmeu88brhbc.streamlit.app/
