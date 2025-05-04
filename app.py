import streamlit as st
import pandas as pd
import time
import plotly.express as px
import os

# Page Config 
st.set_page_config(page_title="Sri Lanka Tourism Services Dashboard", page_icon="🌴")

#  Show Balloons & Progress 
st.balloons()

with st.spinner("Loading data..."):
    time.sleep(1)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'cleaned_Places for Travel-Dining-Recreational activities and Information of travel agents.csv')
df = pd.read_csv(file_path)

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv(file_path)
    return df

df = load_data()


# Sidebar 
st.sidebar.header("🔍 Filter Options")

selected_type = st.sidebar.selectbox("Place Type", [""] + sorted(df["Type"].dropna().unique()))
selected_district = st.sidebar.selectbox("District", [""] + sorted(df["District"].dropna().unique()))
selected_grade = st.sidebar.selectbox("Grade", [""] + sorted(df["Grade"].dropna().unique()))

user_email = st.sidebar.text_input("💌: Enter your email (optional)")

if user_email:
    st.success(f"Thanks for visiting, {user_email}! 🎉")

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
st.caption("Explore restaurants, travel agents & recreational services across districts in Sri Lanka.")

# Summary Metrics 
st.markdown("### 📊 Summary")
col1, col2, col3 = st.columns(3)
col1.metric("📍 Total Places", filtered_df.shape[0])
col2.metric("🔖 Unique Types", df["Type"].nunique())
col3.metric("📌 Districts Covered", df["District"].nunique())

# Charts 
st.markdown("### 📌 Distribution of Place Type")
type_counts = filtered_df["Type"].value_counts().reset_index()
type_counts.columns = ["Type", "Count"]
fig_type = px.bar(type_counts, x="Type", y="Count", color="Type", title="Count by Place Type")
st.plotly_chart(fig_type, use_container_width=True)


st.markdown("### 🥧 Grade Distribution of Places")
grade_counts = filtered_df["Grade"].value_counts().reset_index()
grade_counts.columns = ["Grade", "Count"]
fig_pie = px.pie(grade_counts,names="Grade",values="Count",title="Proportion of Grades Among Places",color_discrete_sequence=px.colors.qualitative.Set3)
st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("### 📈 Grade Distribution as per District")
grade_trend = filtered_df.groupby(['District', 'Grade']).size().reset_index(name='Count')
fig_line = px.line(grade_trend, x="District", y="Count", color="Grade", markers=True, title="Grade Distribution by District")
st.plotly_chart(fig_line, use_container_width=True)


# Data Table 
with st.expander("📂 Show Filtered Raw Data"):
    st.dataframe(filtered_df)



#Footer
st.markdown("---")
st.caption("Developed for Data Science Project Lifecycle module | University of Westminster")

