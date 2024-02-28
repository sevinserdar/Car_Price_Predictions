# import module
import streamlit as st
import joblib
import pandas as pd

# Title
st.title("Car Price Predictions")

# Header
st.header("Learn your car price") 

# Subheader
st.subheader("This is a car predictions app")

# Display Images

st.image("slideshow-564.jpg", caption="Car", width=400)


st.write("İlgilendiğiniz aracın tahmini piyasa değerini aşağıda görebilirsiniz.")

columns = joblib.load("features_list.joblib")

min_year = 2003
max_year = 2018
year = st.number_input("Year: ", min_value=2003, max_value=2018)

min_present_price = 0.1
max_present_price = 100.
present_price = st.slider("Present_Price", min_value=min_present_price, max_value=max_present_price)

min_km = 500
max_km = 500_000
km = st.slider("km", min_value=min_km, max_value=max_km)

fuel_type = st.selectbox(
    'Fuel Type',
    ['Petrol', 'Diesel', 'CNG'])

st.write('You selected', fuel_type)

seller = st.selectbox(
    'Owner',
    ['Dealer', 'Individual'])

st.write('You selected', seller)

transmission = st.selectbox(
    'Transmission',
    ['Manual', 'Automatic'])

st.write('You selected', transmission)

owner = st.selectbox(
    'Owner',
    [0, 1, 3])

st.write('You selected', owner)

sample_one = [{
"Year":year,
"Present_Price":present_price,
"Kms_Driven":km,
"Fuel_Type":fuel_type,
"Seller_Type":seller,
"Transmission":transmission,
"Owner":owner
    }]


df_s = pd.DataFrame(sample_one)
st.dataframe(df_s)

df_s["Year"] = max_year-df_s["Year"]
df_s = pd.get_dummies(df_s).reindex(columns=columns, fill_value=0)

scaler = joblib.load(open("scaler.joblib","rb"))
model = joblib.load(open("xgb_model.joblib","rb"))
df_s = scaler.transform(df_s)

# if st.button("Make Predict"):
#     pred_price = round(model.predict(df_s)[0] * 10_000)
#     st.write(f"Your car's price: ${pred_price}")



# Create a simple button that does nothing
st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
if(st.button("About")):
    pred_price = round(model.predict(df_s)[0] * 10_000)
st.text(f"Your car's price: ${pred_price}")

