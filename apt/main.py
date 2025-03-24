"""
This module provides functionality to download YouTube videos and convert 
them to MP3.
"""

import sys
import yt_dlp
import streamlit as st

def download_video(url, quality='low'):
    try:
        ydl_opts = {
            'format': 'worst' if quality == 'low' else 'best',
            'outtmpl': '%(title)s.%(ext)s'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([url])
        return result
    except Exception as e:
        st.error(f"Error downloading video: {e}")
        return None

def main():
    st.title("Mansa Muz Kingdom of Sound")
    st.write("Loading...")

    st.write("""
    What do you want?

    1. Download YouTube Videos Manually
    2. Download a YouTube Playlist
    3. Download YouTube Videos and Convert Into MP3

    Downloading copyrighted YouTube videos is illegal!
    I am not responsible for your downloads! Do What You Da F Want!

    Copyright (c) M_Group 2025
    """)

    option = st.selectbox(
        'Choose an option:',
        ('Download YouTube Videos Manually', 
         'Download a YouTube Playlist', 
         'Download YouTube Videos and Convert Into MP3')
    )

if __name__ == "__main__":
    main()
    
# Removed invalid import statement as "YT Downloader" is not a valid module name
# Ensure you replace this with the correct module name or path if needed
try:
    pass  # Add your code here if needed
except ImportError:
    print("Error: file_converter module is not available.")
    file_converter = None

"""
#This module provides functionality to download YouTube videos and convert 
them to MP3.
"""

import subprocess
import sys

YTDOWNLOADER_PATH = r"C:\Program Files (x86)\YT Helper\YT Downloader\YTDownloader.exe"

def download_video(url, quality='low'):
    try:
        result = subprocess.run([YTDOWNLOADER_PATH, url, f"--quality={quality}"], 
                              capture_output=True, 
                              text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"Error: {result.stderr}")
            return None
    except Exception as e:
        print(f"Error executing YTDownloader: {e}")
        return None
print("Welcome to Mansa Muz Kingdom of Sound")
print("Loading...")

print('''
What do you want?

(1) Download YouTube Videos Manually
(2) Download a YouTube Playlist
(3) Download YouTube Videos and Convert Into MP3

Downloading copyrighted YouTube videos is illegal!
I am not responsible for your downloads! Do What You Da F Want!

Copyright (c) M_Group 2025
''')


