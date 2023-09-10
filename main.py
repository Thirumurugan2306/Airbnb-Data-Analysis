pip install folium

import pandas as pd
import folium
import streamlit as st

# Load Airbnb dataset
df = pd.read_csv('Airbnb_vis.csv')

# Create a Streamlit web app
st.title("Airbnb Listing Distribution")

st.title('DataFrame Map Visualization')

# Display the DataFrame
st.dataframe(df)

# Create a Folium map
m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=4)

# Add markers to the map
for _, row in df.iterrows():
    folium.Marker([row['latitude'], row['longitude']]).add_to(m)

# Display the map using folium_static
st.write("Map")
st.write(m)
