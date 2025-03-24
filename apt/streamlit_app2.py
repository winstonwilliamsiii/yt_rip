import streamlit as st
st.title("Mansa Muz")
st.markdown(
    """
    <style>
    .title-font {
        color: #F5FFFA;
        font-size: 50px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add Welcome Message
st.subheader("🎵")
st.write("Welcome to Mansa Muz, a music recommendation app that uses Spotify API to recommend songs based on the song you search for. You can also search and download Mp3 files of songs by your favorite artist. Que Chimba!")

st.markdown(
    """ 
    <style>
    .write {
        color: #a9dfbf
        font-size: 20px;
        text-align: bottom;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add custom CSS to change the background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #8b4513;
        background-image: url("https://imagescdn.juno.co.uk/full/CS651426-01A-BIG.jpg");
        background-size: 50%;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add Search Bars
st.sidebar.title("Search Song")
search = st.sidebar.text_input("Search Song")
st.sidebar.title("Search Artist")
search_artist = st.sidebar.text_input("Search Artist")

import streamlit
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import requests
import json
from pytube import YouTube
import urllib.request
from pydub import AudioSegment
from pydub.playback import play

# Spotify API
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    
# Search for a song
if search:
    result = sp.search(search)
    for idx, track in enumerate(result['tracks']['items']):
        st.write(f"{idx+1}. {track['name']} by {track['artists'][0]['name']}")
        st.write(f"Duration: {track['duration_ms']}")
        st.write(f"Popularity: {track['popularity']}")
        st.write(f"Release Date: {track['album']['release_date']}")
        st.write(f"Album: {track['album']['name']}")
        st.write(f"Preview URL: {track['preview_url']}")
        st.write(f"Spotify URL: {track['external_urls']['spotify']}")
        st.write(f"Cover: {track['album']['images'][0]['url']}")
        st.image(track['album']['images'][0]['url'])
        st.write("_______________________________________________________")
        st.write("_______________________________________________________")
        st.write("_______________________________________________________")
        st.write("_______________________________________________________")
        st.write("_______________________________________________________")
        st.write("_______________________________________________________")
        st.write("_______________________________________________________")
        st.write("_______________________________________________________")
        st.write("_______________________________________________________")
        st.write("_______________________________________________________")
        st.write("_______________________________________________________")
        st.write("_______________________________________________________")
        
        
        
        
# Search for an artist
if search_artist:
    result = sp.search(search_artist)
    for idx, artist in enumerate(result['tracks']['items']):
        st.write(f"{idx+1}. {artist['name']}")
        st.write(f"Popularity: {artist['popularity']}")
        st.write(f"Followers: {artist['followers']['total']}")
        st.write(f"Genres: {artist['genres']}")
        st.write(f"Spotify URL: {artist['external_urls']['spotify']}")
        st.write(f"Cover: {artist['images'][0]['url']}")
        st.image(artist['images'][0]['url'])
        st.write("_______________________________________________________")
        st.write("_______________________________________________________")
        st.write("_______________________________________________________")
        
        
# Download Mp3
def download_mp3(url, filename):
    urllib.request.urlretrieve(url, filename)
    st.write(f"Downloaded {filename}")
    
# Download Mp3
def download_mp3(url, filename):
    urllib.request.urlretrieve(url, filename)
    st.write(f"Downloaded {filename}")
    
    # Removed invalid statement
    
    
        
        
        





