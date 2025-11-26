import streamlit as st 
import pandas as pd
import numpy as np

df = pd.read_csv('tips.csv')

# st.dataframe to display dataframes

st.subheader('st.dataframe(data=df,width=1000,height=100)')
st.caption('Display a dataframe as an interactive table')

st.dataframe(data=df,width=1000,height=250)

st.header('st.write(df)')
st.write(df)

# st.static
st.header('st.table')
st.caption('Display a static table')

st.table(data=df.head(5))

# st.json
st.header('st.json')
st.caption('Display object or string as a pretty-printed JSON string')

json_values = df.head(5).to_dict()
#print(json_values)
st.json(json_values)

