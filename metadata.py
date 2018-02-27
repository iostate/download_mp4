# Python 2
import eyed3

# Dependencies for filename
import glob
import os

# Ask for user information

mp3files = glob.glob('/Users/qmtruong92/Music/*.mp3')
latest_file = max(mp3files, key=os.path.getctime)

audio = eyed3.load(latest_file)

str_latest_file = str(latest_file)

# find index of the first -, |, or :
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
