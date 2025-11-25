import streamlit as st
import pandas as pd
import numpy as np

## Title of the aplication
st.title("Hello Streamlit")

## Diplay a Simple Text
st.write("This is a simple text")

##create a simple Dataframe

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})


## Display the Dataframe
st.write("Here is the dataframe")
st.write(df)


##create a line chart
random_numbers=np.random.randn(20,3)
print(random_numbers)
chart_data=pd.DataFrame(
    random_numbers,columns=['a','b','c']
)
st.line_chart(chart_data)