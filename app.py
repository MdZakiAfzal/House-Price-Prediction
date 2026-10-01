import streamlit as st
import json, pickle, numpy as np

st.set_page_config(page_title="Bangalore Real Estate Predictor", page_icon="🏡", layout="centered")
st.title("🏡 Bangalore House Price Predictor")
st.write("Estimate house prices based on location and property size.")

@st.cache_resource
def load_artifacts():
    with open("bangalore_home_prices_model.pickle", "rb") as f:
        model = pickle.load(f)
    with open("columns.json", "r") as f:
        cols = json.load(f)["data_columns"]
    return model, cols

model, data_columns = load_artifacts()
locations = sorted([c for c in data_columns if c not in ["total_sqft", "bath", "bhk"]])

col1, col2 = st.columns(2)
with col1:
    sqft = st.number_input("Total Square Feet", min_value=300, max_value=20000, value=1200, step=50)
    bhk = st.slider("Bedrooms (BHK)", 1, 10, 2)
with col2:
    bath = st.slider("Bathrooms", 1, 10, 2)
    location = st.selectbox("Location", [loc.title() for loc in locations])

if st.button("Predict Price", type="primary"):
    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    
    loc_key = location.lower()
    if loc_key in data_columns:
        loc_index = data_columns.index(loc_key)
        x[loc_index] = 1

    price = model.predict([x])[0]
    st.success(f"Estimated Market Value: ₹ {max(price, 0.0):.2f} Lakhs")
