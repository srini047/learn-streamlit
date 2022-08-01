import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

@st.cache
def load_data():
    data = pd.read_csv(
        "uber-raw-data-sep14.csv.gz",
        nrows=100000,
        names=[
            "date/time",
            "lat",
            "lon",
        ],
        skiprows=1,
        usecols=[0, 1, 2],
        parse_dates=[
            "date/time"
        ],
    )

    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data()
# Notify the reader that the data was successfully loaded.
# data_load_state.text('Loading data...done!')
data_load_state.text("Done! (using st.cache)")

# View the dataframe
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# View the numbber of pickups at every hour
st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data["date/time"].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Map to view all the Pickup Locations
st.subheader('Map of all pickups')
st.map(data)

# st.subheader('Map of Pickup Locations at particular time')
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data["date/time"].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
