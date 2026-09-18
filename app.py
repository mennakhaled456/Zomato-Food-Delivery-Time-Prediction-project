import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

@st.cache_resource
def load_model():
    return joblib.load("rf_delivery_time_model.pkl")

model = load_model()

st.set_page_config(page_title="Delivery Time Predictor", page_icon="🛵")
st.title("🛵 Food Delivery Time Predictor")
st.write("Estimate delivery time based on order conditions, using a Random Forest model trained on the Zomato delivery dataset.")

st.header("Delivery person")
age = st.slider("Delivery person age", 18, 50, 30)
rating = st.slider("Delivery person rating", 1.0, 5.0, 4.6, step=0.1)
vehicle_condition = st.selectbox("Vehicle condition (0 = worst, 2 = best)", [0, 1, 2], index=1)

st.header("Order details")
order_date = st.date_input("Order date", value=datetime.today())
order_time = st.time_input("Order time", value=datetime.now().time())
multiple_deliveries = st.selectbox("Multiple deliveries on this trip?", [0, 1, 2, 3], index=0)
type_of_order = st.selectbox("Type of order", ["Snack", "Meal", "Drinks", "Buffet"])
type_of_vehicle = st.selectbox("Type of vehicle", ["motorcycle", "scooter", "electric_scooter", "bicycle"])
prep_time_minutes = st.slider( "Estimated preparation time (minutes)", 1, 60, 15 )

st.header("Conditions")
distance_km = st.slider("Distance to delivery location (km)", 0.5, 25.0, 8.0, step=0.1)
weather = st.selectbox("Weather conditions", ["Sunny", "Cloudy", "Fog", "Stormy", "Sandstorms", "Windy"])
traffic = st.selectbox("Road traffic density", ["Low", "Medium", "High", "Jam"])
festival = st.selectbox("Festival day?", ["No", "Yes"])
city = st.selectbox("City type", ["Urban", "Metropolitian", "Semi-Urban"])

order_hour = order_time.hour
is_rush_hour = int(order_hour in [12, 13, 19, 20])
order_dayofweek = order_date.weekday()
is_weekend = int(order_dayofweek in [5, 6])

input_row = pd.DataFrame([{
    "Delivery_person_Age": age,
    "Delivery_person_Ratings": rating,
    "distance_km": distance_km,
    "order_hour": order_hour,
    "is_rush_hour": is_rush_hour,
    "order_dayofweek": order_dayofweek,
    "is_weekend": is_weekend,
    "prep_time_minutes": prep_time_minutes,
    "Weather_conditions": weather,
    "Road_traffic_density": traffic,
    "Vehicle_condition": vehicle_condition,
    "Type_of_order": type_of_order,
    "Type_of_vehicle": type_of_vehicle,
    "multiple_deliveries": multiple_deliveries,
    "Festival": festival,
    "City": city,
}])

if st.button("Predict delivery time", type="primary"):
    prediction = model.predict(input_row)[0]
    st.success(f"### Estimated delivery time: {prediction:.1f} minutes")
    with st.expander("See the exact inputs sent to the model"):
        st.dataframe(input_row.T.rename(columns={0: "value"}))