# Made to run in Python 2
# Purpose of the program:
# The purpose of the program is to modify the metadata of a .mp3 file
# When is the file ran:
# The file is made to run after the download.py & bash script
# that downloads a .mp4 or .webm from YouTube, converts it to .mp3
# and then stores it in ~/Music/${filename}.mp3
# EXAMPLE PROGRAM:
# Lines 10 - 19 contain an example of how to use the eyed3 python library
#import eyed3

# audiofile = eyed3.load("song.mp3")
# audiofile.tag.artist = u"Integrity"
# audiofile.tag.album = u"Humanity Is The Devil"
# audiofile.tag.album_artist = u"Integrity"
# audiofile.tag.title = u"Hollow"
# audiofile.tag.track_num = 2

# audiofile.tag.save()
import eyed3  # Python library for working w/ mp3 files

# Dependencies for filename
import glob
import os

# TESTING NOTES:
# This program can be tested with a new .mp3 file in the ~/Music/${NEWEST_FILE}.mp3

# Return a list of all the .mp3 files inside my Music directory
mp3files = glob.glob('/Users/qmtruong92/Music/*.mp3')
# Grab the latest file, based on the OS's ctime, which is the
# seconds elapsed since the epoch
# The file with the largest amount of ctime means that it is the
# newest file in the directory
latest_file = max(mp3files, key=os.path.getctime)

# Load the latest file into eyed3
audio = eyed3.load(latest_file)
# Convert the latest file into a String
str_latest_file = str(latest_file)

# What follows is an attempt to partition the string of the latest file
# into two parts: The artist name & the song name.
# The purpose of splitting the name of the latest file into these two partitions
# is to assign the artist name and the song name to the mp3 metadata.
# Assigning the artist and song name to the mp3 metadata allows
# music indexing software to properly sort the music.

# find index of the first -, |, or :

# The most common separators in a YouTube song name are (in order, first
# to last, most commonly used to least commonly used):
# -,# Made to run in Python 2
# Purpose of the program:
# The purpose of the program is to modify the metadata of a .mp3 file
# When is the file ran:
# The file is made to run after the download.py & bash script
# that downloads a .mp4 or .webm from YouTube, converts it to .mp3
# and then stores it in ~/Music/${filename}.mp3
# EXAMPLE PROGRAM:
# Lines 10 - 19 contain an example of how to use the eyed3 python library
#import eyed3

# audiofile = eyed3.load("song.mp3")
# audiofile.tag.artist = u"Integrity"
# audiofile.tag.album = u"Humanity Is The Devil"
# audiofile.tag.album_artist = u"Integrity"
# audiofile.tag.title = u"Hollow"
# audiofile.tag.track_num = 2

# audiofile.tag.save()
import eyed3  # Python library for working w/ mp3 files

# Dependencies for filename
import glob
import os

# TESTING NOTES:
# This program can be tested with a new .mp3 file in the ~/Music/${NEWEST_FILE}.mp3

# Return a list of all the .mp3 files inside my Music directory
mp3files = glob.glob('/Users/qmtruong92/Music/*.mp3')
# Grab the latest file, based on the OS's ctime, which is the
# seconds elapsed since the epoch
# The file with the largest amount of ctime means that it is the
# newest file in the directory
latest_file = max(mp3files, key=os.path.getctime)

# Load the latest file into eyed3
audio = eyed3.load(latest_file)
# Convert the latest file into a String
str_latest_file = str(latest_file)

# What follows is an attempt to partition the string of the latest file
# into two parts: The artist name & the song name.
# The purpose of splitting the name of the latest file into these two partitions
# is to assign the artist name and the song name to the mp3 metadata.
# Assigning the artist and song name to the mp3 metadata allows
# music indexing software to properly sort the music.

# find index of the first -, |, or :
print("INDEX:" + str(str_latest_file.find('-')))

# The most common separators in a YouTube song name are (in order, first
# to last, most commonly used to least commonly used):
# -, |, :

# Find either -, |, or : in a file

# onehalf = [0,str_latest_file.find('-')] of the latest file string
onehalf = str_latest_file[0:25].encode('utf-8')
secondhalf = str_latest_file[0:len(str_latest_file)].encode('utf-8')

audio.tag.artist = unicode(onehalf)
audio.tag.title = unicode(secondhalf)

print("ARTIST: ")
print audio.tag.artist

print("TITLE: ")
print audio.tag.title
audio.tag.save()

print("INDEX:" + str(str_latest_file.find('-')))

# onehalf = [0,str_latest_file.find('-')] of the latest file string
onehalf = str_latest_file[0:25].encode('utf-8')
secondhalf = str_latest_file[0:len(str_latest_file)].encode('utf-8')

audio.tag.artist = unicode(onehalf)
audio.tag.title = unicode(secondhalf)

print("ARTIST: ")
print audio.tag.artist

print("TITLE: ")
print audio.tag.title
audio.tag.save()
