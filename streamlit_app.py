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
        color: #FFFFFF;
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



