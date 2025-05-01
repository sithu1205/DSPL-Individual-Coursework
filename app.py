import streamlit as st
import pandas as pd
import time
import plotly.express as px

#  Show Balloons & Progress 
st.balloons()

with st.spinner("Loading data..."):
    time.sleep(1)

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("D:\Streamlit\DSPL-Individual-Coursework\cleaned_Places for Travel-Dining-Recreational activities and Information of travel agents.csv")
    return df

df = load_data()
st.success("✅ Data loaded successfully!")

# Sidebar
st.sidebar.header("🔍 Filter Options")
selected_type = st.sidebar.multiselect("Place Type", options=df["Type"].unique(), default=df["Type"].unique())
selected_district = st.sidebar.multiselect("District", options=df["District"].unique(), default=df["District"].unique())
selected_grade = st.sidebar.multiselect("Grade", options=df["Grade"].dropna().unique(), default=df["Grade"].dropna().unique())

user_email = st.sidebar.text_input("💌: Enter your email")

# Apply Filters
filtered_df = df[
    (df["Type"].isin(selected_type)) &
    (df["District"].isin(selected_district)) &
    (df["Grade"].isin(selected_grade))
]

# Main Title 
st.title("🇱🇰 Sri Lanka Tourism Services Dashboard")
st.caption("Explore restaurants, hotels, travel agents & recreational services across districts in Sri Lanka.")



