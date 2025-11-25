import streamlit as st 
import pandas as pd
import os 
from datetime import datetime

with st.form('myform'):

	st.subheader('Registration Form')

	c1, c2, c3 = st.columns(3)
	select_box = c1.selectbox('',('Mr','Mrs','Miss'))
	first_name = c2.text_input('First Name')
	last_name = c3.text_input('Last Name')
	# Role
	role = st.selectbox('Designation',('Software',
		'Sr. Software','Technical Lead',
		'Manager','Sr. Manager','Project Manager'))
	# Date of Birth
	dob = st.date_input('Date of Birth',
		 min_value=datetime(year=1900,month=1,day=1))
	# Gender
	gender = st.radio(
		"Select Gender",
		('Male','Female','Prefered Not to Say')
		)
	# age
	age = st.slider('Age',min_value=1,max_value=100,step=1,value=20)
	submitted = st.form_submit_button('Submit')
	if submitted:
		st.success('Form Subimitted Sucessfully')
		details = {
		'Name': f"{select_box} {first_name} {last_name}",
		'Age': age,
		'Gender':gender,
		'Data of Birth': dob,
		'Designation':role

		}
		st.json(details)





