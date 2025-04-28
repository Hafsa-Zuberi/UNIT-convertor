import streamlit as st

st.set_page_config(page_title="HZ Unit Converter")
st.title('Unit Converter')
st.write("Convert values quickly and accurately across multiple measurement units")

conversion_factors = {
    "Length": {
        "meters": 1,
        "kilometers": 1000,
        "miles": 1609.34,
        "feet": 0.3048,
        "inches": 0.0254,
        "centimeters": 0.01,
        "yards": 0.9144
    },
    "Weight": {
        "grams": 1,
        "kilograms": 1000,
        "pounds": 453.592,
        "ounces": 28.3495
    },
    "Time": {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400
    }
}

category = st.selectbox("Select a category", list(conversion_factors.keys()))
units = list(conversion_factors[category].keys())

value = st.number_input("Enter value")
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)

def convert(value, from_unit, to_unit, factors):
    base = value * factors[from_unit]
    result = base / factors[to_unit]
    return result

if st.button("Convert"):
    answer = convert(value, from_unit, to_unit, conversion_factors[category])
    st.write(value, from_unit, "=", answer, to_unit)
