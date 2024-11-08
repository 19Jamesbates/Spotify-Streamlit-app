# Import necessary libraries
import pandas as pd
import streamlit as st

# Load the CSV file into a DataFrame
try:
    # Load CSV file (make sure 'Spotify.csv' is in the same folder as this Python file)
    df = pd.read_csv('Spotify.csv')
    st.write("File loaded successfully!")
except Exception as e:
    st.error(f"Error loading file: {e}")
    st.stop()  # Stop execution if file loading fails

# Display the title of the app
st.title("Spotify Track Data Explorer")

# Show the first few rows of the DataFrame for reference
st.write("Sample Data:")
st.write(df.head(5))

# Filter and select necessary columns
filtered_data = df[['track_name', 'artist(s)_name', 'released_year', 'released_month', 'released_day', 'streams', 'bpm', 'energy_%', 'cover_url']]

# Handle missing values
filtered_data = filtered_data.dropna(subset=['streams'])

# Sort the data based on user selection
sort_option = st.selectbox(
    'Sort by:',
    ['Most Streams', 'Released Year', 'Released Month', 'Released Day', 'BPM', 'Energy %']
)

# Implement sorting based on user selection
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

# Filter tracks by artist (optional user input)
artist_filter = st.text_input('Filter by artist name (optional):')
if artist_filter:
    sorted_data = sorted_data[sorted_data['artist(s)_name'].str.contains(artist_filter, case=False)]
    if sorted_data.empty:
        st.warning(f"No tracks found for artist: {artist_filter}")

# Display the sorted data
st.subheader(f"Tracks Sorted by {sort_option}")
st.write(sorted_data[['track_name', 'artist(s)_name', 'released_year', 'streams']])

# Display the top 10 tracks
st.subheader("Top 10 Tracks:")
st.write(sorted_data[['track_name', 'artist(s)_name', 'streams']].head(10))

# Display the cover image of the top track if available
if 'cover_url' in sorted_data.columns and not sorted_data['cover_url'].iloc[0].startswith('Not Found'):
    st.image(sorted_data['cover_url'].iloc[0], caption=sorted_data['track_name'].iloc[0])

# Extra Feature: Download sorted data as CSV
st.download_button(
    label="Download Sorted Data as CSV",
    data=sorted_data.to_csv(index=False).encode('utf-8'),
    file_name='sorted_spotify_data.csv',
    mime='text/csv'
)
