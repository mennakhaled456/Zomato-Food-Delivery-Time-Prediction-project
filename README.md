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

This project was completed by a 5-member team:

| Team Member                  | Responsibilities                                                                                                                   |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Menna Allah Khaled Rajab** | Feature Engineering, Main Regression Model, Hyperparameter Tuning, Streamlit Application, Project Coordination & Final Integration |
| **Abdelrahman**              | Data Preprocessing, Exploratory Data Analysis (EDA), Baseline Linear Regression                                                    |
| **Dareen**                   | Data Cleaning Lead, Handling Missing/Invalid Values and Outliers, Decision Tree Regression Model                                   |
| **Salma**                    | Power BI/Tableau Dashboard — Page 1 or Page 2                                                                                      |
| **Maureen**                  | Power BI/Tableau Dashboard — Page 1 or Page 2                                                                                      |

### Menna — Feature Engineering & Main Model

* Calculated actual delivery distance between restaurant and delivery location using latitude and longitude with the **Haversine formula**
* Extracted time-based features such as:

  * Hour of the day
  * Day of the week
  * Peak/rush-hour indicator
* Built the main regression model for predicting `Time_taken`
* Performed model tuning to improve predictive performance
* Developed and deployed the interactive Streamlit prediction application
* Coordinated the integration of the project components and final submission files

### Abdelrahman — Preprocessing, EDA & Baseline Model

* Preprocessed numerical and date/time columns
* Handled missing values
* Converted date/time information into appropriate formats
* Investigated and handled unusual data values
* Performed Exploratory Data Analysis (EDA)
* Analyzed distributions and relationships between delivery time and factors such as weather, traffic, and number of deliveries
* Analyzed correlations between variables
* Built the **Linear Regression baseline model** for comparison with the other regression techniques

### Dareen — Data Cleaning & Decision Tree

* Led the main data-cleaning process
* Handled missing values in important columns such as ratings
* Cleaned incorrect date/time values
* Investigated and handled outliers, including unusual delivery-person ages
* Supported the machine learning stage
* Built a **Decision Tree Regressor** for comparison with the Linear Regression and Random Forest models

### Salma & Maureen — Dashboard

The dashboard component focuses on communicating the project's analytical findings through interactive visualizations.

**Dashboard Page 1 — Geographic, Weather & Traffic Analysis**

* Geographic analysis of restaurant and delivery locations
* Delivery-time patterns by location
* Impact of weather conditions on delivery time
* Impact of traffic conditions on delivery time

**Dashboard Page 2 — Time Trends & City/Festival Analysis**

* Delivery-time trends by hour
* Identification of periods with higher delivery delays
* Comparison between days of the week
* City-type comparisons
* Festival vs. non-festival delivery analysis

The final dashboard file will be added to:

```text
dashboard/
```
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

📊 Data Source

The project uses the Zomato Delivery Operations Analytics Dataset.

Source: Kaggle

Dataset: Zomato Delivery Operations Analytics Dataset

URL:
https://www.kaggle.com/datasets/saurabhbadole/zomato-delivery-operations-analytics-dataset

Access Date: September 18, 2026

The original dataset is included in the repository as:

data/Zomato Dataset.csv

A cleaned version prepared during the project is available as:

data/Zomato_Cleaned_Dareen.csv

The dataset contains information related to food delivery operations, including delivery personnel, restaurants, locations, weather, traffic, order information, and delivery time.

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
