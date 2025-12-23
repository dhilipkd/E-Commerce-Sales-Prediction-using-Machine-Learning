import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title = "E-Commerce Sales Prediction", layout="centered")

model = joblib.load(r'D:\All project set\Projects\ML Project\E-Commerce Sales Prediction\best_model.pkl')
st.markdown("<h1 style='text-align: center; color: #1f77b4;' > E-Commerce Sales Prediction </h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;' > Enter product and order details to predict sales </p>",unsafe_allow_html=True)

st.divider()
st.sidebar.header("Enter Order Details")

year = st.sidebar.number_input("Enter Year", min_value=2011, max_value=2030)
shipment_days = st.sidebar.number_input("Enter Shipment Days", min_value=0, step=1)
ship_mode = st.sidebar.selectbox("Select Ship Mode", ["First Class", "Second Class", "Standard Class","Same day"])
segment = st.sidebar.selectbox("Select Segment", ["Consumer", "Corporate", "Home Office"])
region = st.sidebar.selectbox("Select Region",["Central","East","South","West"])
category = st.sidebar.selectbox("Select Category",["Furniture", "Office Supplies", "Technology"])
sub_category = st.sidebar.text_input("Enter Sub Category")
quantity = st.sidebar.number_input("Enter Quantity",min_value=1,step=1)
discount = st.sidebar.number_input("Enter Discount",min_value=0.0,max_value=1.0,step=0.01)


input_df = pd.DataFrame({
    "Year": [year],
    "shipment days": [shipment_days],
    "Ship Mode": [ship_mode],
    "Segment": [segment],
    "Region": [region],
    "Category": [category],
    "Sub-Category": [sub_category],
    "Quantity": [quantity],
    "Discount": [discount]
})
st.divider()

if st.button("Predict Sales",use_container_width=True ):
    pred = model.predict(input_df)[0]
    st.success(f"Predicted Sales Amount: {pred:,.2f}")