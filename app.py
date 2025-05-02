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


# Sidebar 
st.sidebar.header("🔍 Filter Options")

selected_type = st.sidebar.selectbox("Place Type", [""] + sorted(df["Type"].dropna().unique()))
selected_district = st.sidebar.selectbox("District", [""] + sorted(df["District"].dropna().unique()))
selected_grade = st.sidebar.selectbox("Grade", [""] + sorted(df["Grade"].dropna().unique()))

user_email = st.sidebar.text_input("💌 Optional: Enter your email")

# Apply Filters
filtered_df = df.copy()

if selected_type:
    filtered_df = filtered_df[filtered_df["Type"] == selected_type]

if selected_district:
    filtered_df = filtered_df[filtered_df["District"] == selected_district]

if selected_grade:
    filtered_df = filtered_df[filtered_df["Grade"] == selected_grade]


# Main Title 
st.title("Sri Lanka Tourism Services Dashboard")
st.caption("Explore restaurants, hotels, travel agents & recreational services across districts in Sri Lanka.")

# Summary Metrics 
st.markdown("### 📊 Summary")
col1, col2, col3 = st.columns(3)
col1.metric("📍 Total Places", filtered_df.shape[0])
col2.metric("🔖 Unique Types", df["Type"].nunique())
col3.metric("📌 Districts Covered", df["District"].nunique())

# Charts 
st.markdown("### 📌 Distribution by Place Type")
type_counts = filtered_df["Type"].value_counts().reset_index()
type_counts.columns = ["Type", "Count"]
fig_type = px.bar(type_counts, x="Type", y="Count", color="Type", title="Count by Place Type")
st.plotly_chart(fig_type, use_container_width=True)


st.markdown("### 🥧 Grade Distribution of Places")
grade_counts = filtered_df["Grade"].value_counts().reset_index()
grade_counts.columns = ["Grade", "Count"]
fig_pie = px.pie(grade_counts,names="Grade",values="Count",title="Proportion of Grades Among Places",color_discrete_sequence=px.colors.qualitative.Set3)
st.plotly_chart(fig_pie, use_container_width=True)

# Data Table 
with st.expander("📂 Show Filtered Raw Data"):
    st.dataframe(filtered_df)



