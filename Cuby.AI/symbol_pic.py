import time
import command_speak
from difflib import SequenceMatcher
import os
import pywhatkit

def symbol_picture():
    def matchings(a,b):
        return SequenceMatcher(None , a,b).ratio()
    pics_path = 'pictures/'
    command_speak.speak("name the picture that you want to convert")
    query = command_speak.takecommandexceptional(5)
    query = query.lower()
    pic = query

    matching_song = None
    song_count = 0

    songs = os.listdir(pics_path)
    for file in songs:
        bestest = matchings(pic,file)
        if bestest> song_count:
            matching_song = file
            song_count = bestest
    path = os.path.join(pics_path,matching_song)
    pywhatkit.image_to_ascii_art(path,'pictures//ascii picture')

