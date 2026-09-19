# 🍔 Zomato Food Delivery Time Prediction

A machine learning and data analytics project that analyzes food delivery operations, identifies the main factors affecting delivery time, predicts delivery duration using regression models, and presents the results through an interactive Power BI dashboard and Streamlit application.

---

## 📌 Project Overview

Food delivery time can be influenced by many operational, environmental, geographical, and time-related factors, including:

* Traffic conditions
* Weather conditions
* Delivery distance
* Restaurant preparation time
* Delivery-person characteristics
* Vehicle type and condition
* Multiple deliveries
* Order timing
* Festival days
* City type

The goal of this project is to analyze these factors, identify meaningful patterns, build machine learning models for delivery-time prediction, and deploy the final prediction model through an interactive web application.

---

## 🎯 Business Question

**What factors influence food delivery time, and can machine learning be used to predict the delivery time of a given order?**

The project combines data analytics, machine learning, interactive visualization, and deployment to provide an end-to-end solution for food delivery time prediction.

---

## 📊 Dataset

The project uses the **Zomato Delivery Operations Analytics Dataset** from Kaggle, containing approximately 45,500 food delivery orders.

### Dataset Information

The dataset contains information related to:

* Delivery personnel
* Restaurants
* Order and delivery times
* Weather conditions
* Traffic conditions
* Vehicle type and condition
* Restaurant and delivery coordinates
* Multiple deliveries
* Festival information
* Delivery ratings
* Delivery time

### Dataset Files

| File                             | Description                                    |
| -------------------------------- | ---------------------------------------------- |
| `data/Zomato Dataset.csv`        | Original dataset                               |
| `data/Zomato_Cleaned_Dareen.csv` | Cleaned dataset used for analysis and modeling |

### Data Source

**Kaggle — Zomato Delivery Operations Analytics Dataset**

[Dataset on Kaggle](https://www.kaggle.com/datasets/saurabhbadole/zomato-delivery-operations-analytics-dataset)

**Access Date:** September 18, 2026

---

# 🔄 Project Workflow

The project follows an end-to-end data science and machine learning workflow:

```text
Raw Dataset
     ↓
Data Cleaning & Preprocessing
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Machine Learning Models
     ↓
Hyperparameter Tuning
     ↓
Model Evaluation
     ↓
Power BI Dashboard
     ↓
Streamlit Deployment
     ↓
Final Delivery-Time Prediction System
```

---

## 1. Data Collection

The Zomato Delivery Operations Analytics Dataset was collected from Kaggle and prepared for analysis.

The original dataset is included in the repository under:

```text
data/Zomato Dataset.csv
```

---

## 2. Data Cleaning & Preprocessing

The dataset was prepared before analysis and modeling.

The preprocessing stage included:

* Handling missing values
* Removing duplicate records
* Handling invalid or unusual values
* Processing date and time information
* Checking numerical features
* Handling categorical variables
* Validating geographical information
* Preparing the cleaned dataset for analysis and machine learning

The cleaned dataset is available at:

```text
data/Zomato_Cleaned_Dareen.csv
```

---

## 3. Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the distribution of the data and investigate relationships between delivery time and operational factors.

The analysis included:

* Distribution analysis
* Correlation analysis
* Categorical analysis
* Numerical summaries
* Delivery-time relationships
* Weather analysis
* Traffic analysis
* Multiple-delivery analysis
* Vehicle analysis
* City analysis
* Festival vs. non-festival analysis

---

# 🛠️ 4. Feature Engineering

Additional features were created to improve the analysis and predictive modeling.

### Delivery Distance

The actual distance between the restaurant and delivery location was calculated using geographical latitude and longitude coordinates.

The **Haversine formula** was used to calculate the approximate geographical distance in kilometers.

### Time-Based Features

The project also extracted:

* Hour of the day
* Day of the week
* Weekend indicator
* Rush-hour / peak-time indicator

Additional operational features were also prepared for the machine learning models.

---

# 🤖 5. Machine Learning

Three regression approaches were evaluated:

| Model                         | Purpose                          |
| ----------------------------- | -------------------------------- |
| Linear Regression             | Baseline regression model        |
| Decision Tree Regressor       | Non-linear regression comparison |
| Tuned Random Forest Regressor | Final prediction model           |

The target variable is:

```text
Time_taken
```

---

## 📈 Model Evaluation

The models were evaluated using:

* **MAE — Mean Absolute Error**
* **RMSE — Root Mean Squared Error**
* **R² — Coefficient of Determination**

### Model Performance

| Model                 |          MAE |         RMSE |           R² |
| --------------------- | -----------: | -----------: | -----------: |
| Linear Regression     |     4.771415 |     6.001154 |     0.582788 |
| Decision Tree – Tuned |     3.378057 |     4.333443 |     0.782453 |
| Random Forest – Tuned | **3.219338** | **4.079978** | **0.807157** |

Among the evaluated models, the tuned Random Forest achieved the lowest MAE and RMSE and the highest R².

The trained Random Forest model is stored in:

```text
rf_delivery_time_model.pkl
```

The complete modeling workflow is available in:

```text
notebooks/zomato_food_delivery.ipynb
```

---

# 🖥️ 6. Streamlit Application

The final trained Random Forest model was integrated into an interactive Streamlit application.

Users can enter information such as:

* Delivery-person age
* Delivery-person rating
* Vehicle condition
* Order date and time
* Multiple deliveries
* Order type
* Vehicle type
* Restaurant preparation time
* Delivery distance
* Weather conditions
* Traffic conditions
* Festival status
* City type

The application then uses the trained machine learning model to estimate the expected delivery time.

### 🚀 Live Application

[Open the Streamlit Application](https://zomato-food-delivery-time-prediction-project-hu6scvwmeu88brhbc.streamlit.app/)

### Application Files

```text
app.py
rf_delivery_time_model.pkl
requirements.txt
```

---

# 📊 7. Power BI Dashboard

The project includes an interactive **four-page Power BI dashboard** designed to provide business-level insights into food delivery operations.

The dashboard analyzes delivery performance, operational and environmental conditions, driver and timing relationships, and geographical patterns.

---

## Page 1 — Executive Overview

The first page provides a high-level summary of the overall delivery operation.

### KPI Cards

* **Total Orders**
* **Average Delivery Time**
* **Median Delivery Time**
* **Average Delivery Rating**
* **Slow Delivery %**

### Visualizations

* Delivery-time trend by month
* Orders by city
* Average delivery time across traffic-density levels
* Delivery Performance donut chart

### Interactive Slicers

* Vehicle type
* Date
* Traffic
* City
* Weather

This page serves as the landing and executive summary page of the dashboard.

---

## Page 2 — Conditions & Vehicle Impact

This page focuses on the operational and environmental factors associated with delivery time.

### Analysis Includes

Average delivery time comparisons across:

* Weather conditions
* Road traffic density
* Vehicle type
* Vehicle condition
* Multiple-deliveries count

The page also includes a comparison between:

* Festival deliveries
* Non-festival deliveries

### Interactive Slicers

* City
* Weather
* Traffic
* Vehicle type
* Date

This page helps investigate how environmental and operational conditions relate to delivery performance.

---

## Page 3 — Driver & Timing Relationships

This page explores relationships between driver characteristics, delivery ratings, restaurant pickup delay, and delivery time.

### Scatter Plots

1. **Delivery-person age vs. time taken**
2. **Delivery rating vs. time taken**
3. **Pickup delay vs. time taken**

### Detailed Relationship Tables

* Traffic × Vehicle Type → Average Delivery Time
* Weather × Traffic → Average Delivery Time

These visualizations provide both relationship-based and numerical analysis of delivery performance.

---

## Page 4 — Geographic View

This page focuses on geographical and city-level delivery analysis.

### Geographic Visualization

A map visual uses restaurant latitude and longitude coordinates to display restaurant locations.

The map provides contextual information such as:

* Order volume
* Average delivery time
* Delivery rating

### City-Level Analysis

* Average delivery time by city
* Order volume by city

### Detailed Relationship Tables

* Traffic × City
* Vehicle Type × City

This page provides a geographical perspective on the delivery operation and directly uses the coordinate data.

---

## 📁 Dashboard File

The Power BI dashboard is available in:

```text
dashboard/zomato final.pbix
```

---

# 📁 Project Structure

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
│   └── zomato final.pbix
│
├── report/
│   └── Final project report
│
└── presentation/
    └── Zomato_Delivery_Time_Prediction_Presentation.pptx
```

---

# 🛠️ Technologies Used

### Programming & Data Analysis

* Python
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Power BI

### Machine Learning

* Scikit-learn
* Linear Regression
* Decision Tree Regression
* Random Forest Regression

### Deployment & Development

* Jupyter Notebook
* Streamlit
* Git
* GitHub

---

# ▶️ Run the Project Locally

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

# 📓 Notebook

The complete machine learning workflow is available in:

```text
notebooks/zomato_food_delivery.ipynb
```

The notebook covers:

* Data preparation
* Exploratory Data Analysis
* Feature engineering
* Model training
* Model tuning
* Model evaluation

---

# 👥 Team

This project was completed by a five-member team.

| Team Member             | Responsibilities                                                                                                                   |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Dareen Alaa**         | Data Cleaning Lead, missing/invalid values and outlier handling, Decision Tree Regression                                          |
| **Salma Tarek**         | Power BI measurements and DAX calculations, relationship modeling, and dashboard support                                           |
| **Moureen Ramy Kelada** | Complete Power BI dashboard development across all four pages                                                                      |
| **Menna Khaled**        | Feature Engineering, Main Regression Model, Hyperparameter Tuning, Streamlit Application, Project Coordination & Final Integration |
| **Abdelrahman Mahmoud** | Data Preprocessing, Exploratory Data Analysis, Baseline Linear Regression                                                          |

---

## 👩‍💻 Menna Khaled — Feature Engineering & Main Model

* Calculated actual restaurant-to-delivery distance using latitude and longitude
* Applied the Haversine formula for distance calculation
* Extracted time-based features
* Created hour-of-day features
* Created day-of-week features
* Created peak/rush-hour indicators
* Built the main regression model for predicting `Time_taken`
* Performed model and hyperparameter tuning
* Developed the Streamlit prediction application
* Coordinated the integration of the project components and final submission

---

## 👩‍💻 Dareen Alaa — Data Cleaning & Decision Tree

* Led the main data-cleaning process
* Handled missing values
* Cleaned incorrect date/time values
* Investigated unusual values and outliers
* Worked with delivery-person data
* Supported the machine learning stage
* Built the Decision Tree Regressor for model comparison

---

## 👩‍💻 Salma Tarek — Power BI Data Modeling & Measurements

* Developed Power BI measurements and DAX calculations
* Worked on relationship modeling between project tables
* Supported the Power BI dashboard development
* Assisted the team with Power BI implementation and analytical requirements

---

## 👩‍💻 Moureen Ramy Kelada — Power BI Dashboard Development

Moureen developed the complete four-page Power BI dashboard covering:

* Executive Overview
* Conditions & Vehicle Impact
* Driver & Timing Relationships
* Geographic View

The dashboard combines KPI cards, charts, scatter plots, pivot-style tables, slicers, and geographical visualization to communicate the project's analytical findings.

---

## 👨‍💻 Abdelrahman Mahmoud — Preprocessing, EDA & Baseline Model

* Preprocessed numerical and date/time columns
* Handled missing values
* Converted date/time information
* Investigated unusual data values
* Performed Exploratory Data Analysis
* Analyzed delivery-time relationships with weather, traffic, and number of deliveries
* Analyzed correlations between variables
* Built the Linear Regression baseline model

---

# 📚 Project Documentation

The final project documentation includes a written report and presentation covering the project methodology, analysis, machine learning models, dashboard, findings, and conclusions.

### Written Report

The report covers:

* Business question
* Dataset and data source
* Data preparation
* Exploratory Data Analysis
* Feature engineering
* Machine learning methodology
* Model evaluation
* Dashboard analysis
* Key findings
* Limitations
* Conclusion
* References
* Project links

The report is included under:

```text
report/
```

### Project Presentation

The final project presentation is included under:

```text
presentation/Zomato_Delivery_Time_Prediction_Presentation.pptx
```

The presentation summarizes the project's:

* Business problem
* Dataset
* Data preparation
* Exploratory analysis
* Feature engineering
* Machine learning models
* Model evaluation
* Power BI dashboard
* Streamlit application
* Key findings
* Conclusion

---

# ⚠️ Limitations

Machine learning predictions depend on the quality and characteristics of the available training data.

Actual delivery times may also be affected by factors that are not represented in the dataset, including:

* Unexpected traffic events
* Operational issues
* Restaurant delays
* Sudden weather changes
* Driver availability
* Other real-world delivery conditions

Therefore, model predictions should be considered estimates rather than guaranteed delivery times.

---

# 📌 Project Status

| Component                 | Status        |
| ------------------------- | ------------- |
| Data Collection           | ✅ Complete    |
| Data Cleaning             | ✅ Complete    |
| Exploratory Data Analysis | ✅ Complete    |
| Feature Engineering       | ✅ Complete    |
| Machine Learning          | ✅ Complete    |
| Model Tuning              | ✅ Complete    |
| Model Deployment          | ✅ Complete    |
| Streamlit Application     | ✅ Live        |
| Power BI Dashboard        | ✅ Complete    |
| Project Presentation      | ✅ Complete    |
| Written Report            | ⏳ In Progress |

---

# 🔗 Project Links

| Resource                   | Link / Location                                                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| GitHub Repository          | [Zomato Food Delivery Time Prediction](https://github.com/mennakhaled456/Zomato-Food-Delivery-Time-Prediction-project) |
| Live Streamlit Application | [Open Streamlit App](https://zomato-food-delivery-time-prediction-project-hu6scvwmeu88brhbc.streamlit.app/)            |
| Power BI Dashboard         | `dashboard/zomato final.pbix`                                                                                          |
| Project Notebook           | `notebooks/zomato_food_delivery.ipynb`                                                                                 |
| Project Report             | `report/`                                                                                                              |
| Project Presentation       | `presentation/Zomato_Delivery_Time_Prediction_Presentation.pptx`                                                                                                        |

---

# ⭐ Project Summary

This project combines **data cleaning, exploratory analysis, feature engineering, machine learning, Power BI analytics, and Streamlit deployment** into an end-to-end food delivery prediction system.

The project demonstrates how operational, environmental, geographical, and time-related delivery data can be transformed into analytical insights and machine learning predictions that support the understanding and prediction of food delivery performance.
