# This program takes two playlists and creates a new playlist with the songs that are in both playlists.

import re

# absolute/relative path to the playlists
url1 = "PlaylistOverlap\\Favorites.m3u"
url2 = "PlaylistOverlap\\Chill.m3u"

# read the playlists and store the songs in 2 dictionaries
with open(url1, "r", encoding="utf8") as f:
    data = f.read()
    songs = {}
    for i in range(0, len(data.split("\n"))-1, 2):
        try:
            songs[data.split("\n")[i+1]] = data.split("\n")[i+2]
        except IndexError:
            pass

with open(url2, "r", encoding="utf8") as f:
    data = f.read()
    songs2 = {}
    for i in range(0, len(data.split("\n"))-1, 2):
        try:
            songs2[data.split("\n")[i+1]] = data.split("\n")[i+2]
        except IndexError:
            pass

# create a new dictionary with the songs that are in both playlists
overlapping_songs = {}

for song in songs:
    if song in songs2:
        overlapping_songs[song] = songs[song]

# write the new playlist
with open("PlaylistOverlap\\overlapping_songs.m3u", "w", encoding="utf8") as f:
    f.write("#EXTM3U\n")
    for song in overlapping_songs:
        f.write(song + "\n")
        f.write(overlapping_songs[song] + "\n")
        