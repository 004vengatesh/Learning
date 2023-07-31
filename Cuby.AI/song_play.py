from difflib import SequenceMatcher
import os
import command_speak
import pyjokes

def playsongs(query):
    def matchings(a,b):
        return SequenceMatcher(None , a,b).ratio()
    song_path = 'songs'
    song = query

    matching_song = None
    song_count = 0

    songs = os.listdir(song_path)
    for file in songs:
        bestest = matchings(song,file)
        if bestest> song_count:
            matching_song = file
            song_count = bestest
    path = os.path.join(song_path,matching_song)
    os.startfile(path)

def jokes():
    command_speak.speak(pyjokes.get_joke(category='all'))
