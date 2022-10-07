import streamlit as st
import pandas as pd
import pickle
import sklearn

model = pickle.load(open('model.pkl', 'rb'))

st.title("Walmart Sales Prediction")
# 'Store','Fuel_Price','CPI','Unemployment','Day','Month','Year'
col1, col2 = st.columns(2)
with col1:
    store_ds = st.number_input("Enter Store No (From 1 to 45)")
with col2:
    fuel_price = st.number_input("Enter Fuel Price")
col3, col4, col5 = st.columns(3)
with col3:
    CPI = st.number_input("Enter CPI")
with col4:
    Unemployment = st.number_input("Enter Unemployment")
with col5:
    date = st.date_input("Enter date")

day_ds = date.day
month_ds = date.month
year_ds = date.year

if st.button('Predict Sales'):
    input_df = pd.DataFrame(
        {'Store': [store_ds], 'Fuel_Price': [fuel_price], 'CPI': [CPI],
         'Unemployment': [Unemployment], 'Day': [day_ds], 'Month': [month_ds], 'Year': [year_ds]})
    prediction = model.predict(input_df)
    answer = "Estimated sales for " + str(date) + " is: " + str(round(prediction[0])) + " USD"
    st.subheader(answer)






