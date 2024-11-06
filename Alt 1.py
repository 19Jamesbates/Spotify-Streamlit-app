# Import necessary libraries
import pandas as pd
import streamlit as st

# Load the CSV file into a DataFrame
df = pd.read_csv('Spotify.csv')

# Select only the required columns
filtered_data = df[['track_name', 'artist(s)_name', 'released_year', 'released_month', 'released_day', 'streams', 'bpm', 'energy_%', 'cover_url']]

# Handle missing values in the 'streams' column
filtered_data = filtered_data.dropna(subset=['streams'])

# Sort the data based on user selection
st.title("Spotify Track Data")

sort_option = st.selectbox(
    'Sort by:',
    ['Most Streams', 'Released Year', 'Released Month', 'Released Day', 'BPM', 'Energy %']
)

if sort_option == 'Most Streams':
    sorted_data = filtered_data.sort_values(by='streams', ascending=False)
elif sort_option == 'Released Year':
    sorted_data = filtered_data.sort_values(by='released_year', ascending=False)
elif sort_option == 'Released Month':
    sorted_data = filtered_data.sort_values(by='released_month', ascending=False)
elif sort_option == 'Released Day':
    sorted_data = filtered_data.sort_values(by='released_day', ascending=False)
elif sort_option == 'BPM':
    sorted_data = filtered_data.sort_values(by='bpm', ascending=False)
else:  # Energy %
    sorted_data = filtered_data.sort_values(by='energy_%', ascending=False)

# Format the 'streams' column for better readability
sorted_data['streams'] = sorted_data['streams'].apply(lambda x: f'{int(x):,}')

# Display the sorted data
st.write(sorted_data)

# Optional: Display the cover image for the top track
st.image(sorted_data['cover_url'].iloc[0])  # Display cover of the top track

# Display the top N tracks (e.g., top 10)
st.write("Top 10 Tracks:")
st.write(sorted_data.head(10))
