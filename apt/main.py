"""
This module provides functionality to download YouTube videos and convert 
them to MP3.
"""

import sys
""



import sys
from yt-dlp import YouTube  # A common YouTube download library


# Define the downloader function
def download_video(url, quality='low'):
    try:
        yt = YouTube(url)
        if quality == 'low':
            video = yt.streams.get_lowest_resolution()
        elif quality == 'high':
            video = yt.streams.get_highest_resolution()
        else:
            video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        
        return video.download()
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None
# Removed invalid import statement as "YT Downloader" is not a valid module name
# Ensure you replace this with the correct module name or path if needed
try:
    import file_converter
except ImportError:
    print("Error: file_converter module is not available.")
    file_converter = None

"""
This module provides functionality to download YouTube videos and convert 
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


