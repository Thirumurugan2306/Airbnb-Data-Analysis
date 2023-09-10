import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
import pandas as pd
from pymongo import MongoClient
from geopy.geocoders import Nominatim
from bson import Decimal128 

df=pd.read_csv("Airbnb.csv")

print(df.columns)
st.title("Airbnb Data Analysis and Visualization")
st.write("Explore Airbnb listing data interactively.")





# Display the map using st.write()
