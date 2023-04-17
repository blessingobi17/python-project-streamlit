import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

def get_data():
    PROJECT="datasets/obi_blessing_project.csv"
    data=pd.read_csv(PROJECT)
    return data

try:
    data=get_data()
    st.title("Global Food Prices")
    
    # st.write(df)
    st.write(data.head(10))
    st.title("Global Food Prices - Nigeria")
    grp_country=data.groupby("Country_name")
    st.write(grp_country.get_group("Nigeria"))

    # side bar
    with st.sidebar:
        st.subheader("pick a country to view more details")
        selected_country=st.selectbox("Select a country",list(data.Country_name.unique()))
    selected_country_details=grp_country.get_group(selected_country)
    st.subheader(f"{selected_country} market types")
    st.write(selected_country_details[["Country_name","Market_name"]].head(5))
  
    if selected_country:
        with st.sidebar:
            st.subheader("Pick a commodity")
            lang=st.multiselect("Select Commodity", ["Wheat flour","Sugar", "Potatoes", "Oil"])
        used_selected_lang=selected_country_details["Commodity_purchased"].str.split(';')
    
    
except:
    pass


# pie chart, top 10 countries
pie_data=data["Country_name"].value_counts().head(10)
st.write(pie_data)
fig1, ax1=plt.subplots(figsize=(10,8))
ax1.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%")
st.subheader(
"""Top 10 country purchases"""
)
st.pyplot(fig1)