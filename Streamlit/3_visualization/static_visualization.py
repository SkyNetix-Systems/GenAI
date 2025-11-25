import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.header("Simple Visualization App")
df = pd.read_csv("tips.csv")

st.subheader("Data Preview")
st.dataframe(df.head())

# ----------------------------
# 1. Pie + Bar Chart for Sex
# ----------------------------
st.markdown("---")
st.subheader("1. Male vs Female Distribution")

value_counts = df["sex"].value_counts()

col1, col2 = st.columns(2)

with col1:
    st.write("Pie Chart")
    fig, ax = plt.subplots()
    ax.pie(value_counts, labels=value_counts.index, autopct="%0.2f%%")
    st.pyplot(fig)

with col2:
    st.write("Bar Chart")
    fig, ax = plt.subplots()
    ax.bar(value_counts.index, value_counts)
    st.pyplot(fig)

# ----------------------------
# 2. Distribution of Spending
# ----------------------------
st.markdown("---")
st.subheader("2. Distribution of Total Bill by Gender")

chart_type = st.selectbox("Choose Chart Type", ["box", "violin", "kde", "hist"])

fig, ax = plt.subplots()

if chart_type == "box":
    sns.boxplot(x="sex", y="total_bill", data=df, ax=ax)
elif chart_type == "violin":
    sns.violinplot(x="sex", y="total_bill", data=df, ax=ax)
elif chart_type == "kde":
    sns.kdeplot(data=df, x="total_bill", hue="sex", ax=ax)
else:
    sns.histplot(data=df, x="total_bill", hue="sex", ax=ax)

st.pyplot(fig)
