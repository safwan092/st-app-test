import folium
import streamlit as st
from streamlit_folium import st_folium

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button


st.title("Interactive Page")
st.write("Welcome to this App")
st.button('Click me', on_click=click_button)


if st.session_state.button:
    st.title("")
    # The message and nested widget will remain on the page
    m = folium.Map(location=[21.502771, 39.247194], zoom_start=18)
    folium.Marker = m.add_child(folium.ClickForMarker("<b>Lat: </b> ${lat}<br/><b>Lon: </b> ${lng}<br><b>Altitude:</b> 10.00 m"))
    output = st_folium(m, width=700, height=500)
    if output["last_clicked"] is not None:
        output["last_clicked"]["alti"] = 10
        latitude_1_last_clicked    = round(output["last_clicked"]["lat"], 6)
        longitude_1_last_clicked   = round(output["last_clicked"]["lng"], 6)
        altitude_1_last_clicked    = output["last_clicked"]["alti"]
        st.write("• Latitude:", latitude_1_last_clicked)
        st.write("• Latitude:", longitude_1_last_clicked)
        st.write("• Altitude:", altitude_1_last_clicked, "meter")
