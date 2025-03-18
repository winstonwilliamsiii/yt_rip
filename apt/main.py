"""
This module provides functionality to download YouTube videos and convert 
them to MP3.
"""

import sys
sys.path.append("C:/ProgramFiles(x86)/YTHelper/YTDownloader")

import ytdownloader
try:
    import file_converter
except ImportError:
    print("Error: file_converter module is not available.")
    file_converter = None

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

choice = input("Choice: ")

if choice == "1" or choice == "2":
    quality = input("Please choose a quality (low, medium, high, very high):")
    if choice == "2":
        link = input("Enter the link to the playlist: ")
        print("Downloading playlist...")
        ytdownloader.download_playlist(link, quality)
        print("Download finished!")
    if choice == "1":
        links = ytdownloader.input_links()
        for link in links:
            ytdownloader.download_video(link, quality)
elif choice == "3":
    links = ytdownloader.input_links()
    for link in links:
        print("Downloading...")
        filename = ytdownloader.download_video(link, 'low')
        print("Converting...")
        file_converter.convert_to_mp3(filename)
else:
    print("Invalid input! Terminating...")
