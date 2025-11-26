import streamlit as st
import pandas as pd
import plotly.express as px

# Load CSV file into a Pandas DataFrame
df = pd.read_csv("tips.csv")  # contains restaurant bill + tip info

# App title
st.title("Tips Data Visualizations")

# ----------------------------------------------------------
# 1️⃣ Histogram: Distribution of total bills
# ----------------------------------------------------------
st.subheader("1. Histogram of Total Bill")

# Create basic histogram (shows frequency of total_bill values)
fig = px.histogram(df, x="total_bill")

# Display plot (key prevents Streamlit ID conflict)
st.plotly_chart(fig, key="hist1")

# ----------------------------------------------------------
# 2️⃣ Histogram grouped by sex
# ----------------------------------------------------------
st.subheader("2. Total Bill by Sex")

# Adding 'color' splits the bars by male/female
fig = px.histogram(df, x="total_bill", color="sex")
st.plotly_chart(fig, key="hist2")

# ----------------------------------------------------------
# 3️⃣ Histogram with selectable category
# ----------------------------------------------------------
st.subheader("3. Total Bill by Category")

# Dropdown lets the user choose which column to group by
color_by = st.selectbox(
    "Color by:",
    ("sex", "smoker", "day", "time"),
    index=0  # default = sex
)

# Visualization updates based on the selected option
fig = px.histogram(df, x="total_bill", color=color_by)
st.plotly_chart(fig, key="hist3")

# ----------------------------------------------------------
# 4️⃣ Scatter Plot: Total Bill vs Tip
# ----------------------------------------------------------
st.subheader("4. Scatter: Total Bill vs Tip")

# Dropdown controls color grouping for scatter plot points
scatter_color = st.selectbox(
    "Color points by:",
    ("sex", "smoker", "day", "time"),
    index=0
)

# Shows relationship between bill amount and tip amount
fig = px.scatter(df, x="total_bill", y="tip", color=scatter_color)
st.plotly_chart(fig, key="scatter1")

# ----------------------------------------------------------
# 5️⃣ Sunburst Chart: Hierarchical Path
# ----------------------------------------------------------
st.subheader("5. Sunburst Chart")

# User picks multiple categorical levels for hierarchy
path = st.multiselect(
    "Select hierarchy:",
    ("sex", "day", "smoker", "time"),
    default=["sex", "day"]  # default first two levels
)

# Sunburst shows proportional breakdown in a nested structure
fig = px.sunburst(df, path=path)
st.plotly_chart(fig, key="sunburst1")
