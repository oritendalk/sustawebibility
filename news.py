import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
st.header("Maps")
data = pd.DataFrame({
    'latitude': [ 33.7723, 33.749, 33.77282, 33.77265],
    'longitude': [ -84.4027, -84.38798, -84.3823, -84.3806],
    'location': ['Goodwill Thrift Store & Donation Center', 'The Salvation Army Adult Rehabilitation Center - Atlanta', 'Goodwill Donation Center', 'The Lucky Exchange'],
    'color': ['#4287f5', '#4bb352', '#9e3a16', '#a34396'],
})
st.map(data, zoom =13, color='color')
