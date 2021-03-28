import pandas as pd
import streamlit as st

data = pd.read_csv('Debt_GDP_World.csv')

st.title("Comparing GDP to Debt Ratio of Different Countries!")
st.subheader("We will be comparing diiferent countrie's GDP to Debt Ratio to see if we can mind any comparitive similarities or disparities in Policy Making which makes them different.")




