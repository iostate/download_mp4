import requests

# !/usr/local/bin/pyhon
from pytube import YouTube

print('*****************Enter the YouTube URL*****************:')
# # https://www.youtube.com/watch?v=X7DpJpMmFys&list=RDX7DpJpMmFys&t=330
# the above link fails on line 11
url = str(input())
yt = YouTube(url)

# Store some data about the downloaded song
video_title = yt.title
album_cover_art_url = yt.thumbnail_url

# Download the album cover and store it in current working directory
# Implement error handling - is it needed?
print("*****************Downloading cover art*****************")
album_cover_art_image = open('albumcover.jpg', 'wb')
album_cover_art_image.write(requests.get(album_cover_art_url).content)
album_cover_art_image.close()

print("*****************THUMBNAIL URL = " + album_cover_art_url)
print("*****************TITLE: " + video_title)

# Download the first stream and save it in the working directory with
# the original YouTube title
yt.streams.first().download(None, filename=video_title)
print("*****************Download has finished!*****************")


print("\n\n\n")
print("*****************BEGIN BASH SCRIPT*****************")



# Download the first stream of this file and save it as craptds (the slashes
# are not recognized) in the current directory. .
# The downloaded stream will either be a .webm or .mp4
# yt.streams.first().download(None, filename='\/crap\/tds')
# print('Download finished!')

# Improvements that need to be made:
# Learn to save the resulting mp3 file as the name of the YouTube title
# Learn how to create the bash script (check below) and to run it in python

# Does this code open up a different shell?
# !/bin/sh
# python3 /Users/qmtruong92/Code/PythonProjects/DownloadMP4/pytube_dl_video.py
# ffmpeg -i tds.mp4 filename.mp3
