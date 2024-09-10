import folium
import streamlit as st
from streamlit_folium import folium_static

st.set_page_config(layout="centered", page_icon='🌎')
st.image('https://upload.wikimedia.org/wikipedia/en/d/d2/National_Disaster_Response_Force_Logo.png', width=80)

st.title("Control Desk")

col1, col2 = st.columns(2)
with col1:
    var = st.selectbox('Event', ['Earthquake', 'Volcanic_Eruption', 'Hurricanes', 'Floods'])
    
with col2:
    location = st.selectbox('Location', ['Location 1', 'Location 2', 'Location 3', 'Location 4'])

# Coordinates for each location
coordinates = {
    'Location 1' : [41.894267774731894, 12.46313955769402],
    'Location 2' : [48.865964982032985, 2.291400401109551],
    'Location 3' : [41.90194423963293, 12.453944956543546],
    'Location 4' : [12.924124614696765, 100.87878978786833]
}

# Get coordinates of the selected location
selected_coordinates = coordinates.get(location)

# Create a Folium map centered on the selected location
m = folium.Map(location=selected_coordinates, tiles='Cartodb Positron', zoom_start=14.3)

# Custom icons for events
event_icons = {
    'Earthquake': folium.CustomIcon(icon_image="res/earthquake.png", icon_size=(50, 50)),
    'Volcanic_Eruption': folium.CustomIcon(icon_image="res/volcano.png", icon_size=(50, 50)),
    'Hurricanes': folium.CustomIcon(icon_image="res/hurricane.png", icon_size=(50, 50)),
    'Floods': folium.CustomIcon(icon_image="res/tide.png", icon_size=(50, 50))
}

# Get the appropriate icon based on the selected event
selected_icon = event_icons.get(var, folium.Icon(icon='info-sign'))  # Default to a basic icon if not found

# Add a marker with the selected icon at the selected location
folium.Marker(selected_coordinates, popup=f"{var} Marker", icon=selected_icon).add_to(m)

# Display the map
folium_static(m)
