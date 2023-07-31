import command_speak 
import pywhatkit
import pyautogui as py
import time
import os
import song_play
import cpu_ss
import symbol_pic
import wp
import control_pan
import this_pc
import writter
import main_file


def main_2(query,query_1):
    while True:
        if 'restart my pc' in query:
            command_speak.speak('warning! it will restart your system. please confirm the command, say yes to continue')
            lock = command_speak.takecommandexceptional(5)
            if 'yes' in lock:
                os.system('C:\\Windows\\System32\\shutdown.exe /r /t 0')
            else:
                command_speak.speakinput()
        elif 'play offline songs' in query :
            songs_dir = 'songs'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif 'play' in query:
            query = query.lower()
            query = query.replace('play','')
            song_play.playsongs(query)
        elif 'remember that' in query:
            query = query.replace('remember that','')
            command_speak.speak("you said me to remember"+query)
            remember = open('data.txt','w')
            remember.write(query)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            command_speak.speak("you said me to remember that" +remember.read())
        elif 'joke' in query:
            song_play.jokes()
        elif 'cpu' in query:
            cpu_ss.cpu()
        elif 'battery' in query:
            cpu_ss.cpu()
        elif 'symbol' in query:
            symbol_pic.symbol_picture()
        elif 'screenshot' in query:
            cpu_ss.screenshot()
            command_speak.speak("done!")
        elif 'whatsapp' in query:
            command = query
            py.click(200, 950)
            time.sleep(3)
            py.write('whatsapp')
            time.sleep(4)
            py.press('enter')
            time.sleep(3)
            wp.whatsapp()
        elif 'minimize' in query:
            py.click(1250,20)
        elif 'maximize' in query:
            py.hotkey("win","up")
        elif 'youtube' in query:
            query = query.replace('youtube','')
            pywhatkit.playonyt(query)
        elif 'settings' in query:
            control_pan.controlpannel()
        elif 'this pc' in query:
            py.click(300, 800)
            time.sleep(5)
            py.write('this pc')
            time.sleep(3)
            py.press('enter')
            this_pc.thispc()
        elif 'select all' in query:
            py.hotkey('ctrl', 'a')
        elif 'save with custom name' in query:
            py.hotkey('ctrl', 's')
        elif 'save' in query:
            py.hotkey('ctrl', 's')
            time.sleep(2)
            py.write(query_1)
            time.sleep(2)
            py.press("enter")
        elif 'press' in query:
            query = query.lower()
            query = query.replace('press ','')
            py.press(query)
        elif 'writer' in query:
            writter.writter()
        elif 'handwritten' in query:
            writter.handwrittens()
        elif 'go to' in query:
            py.click(200,800)
            time.sleep(5)
            query = query.replace('go to','')
            py.write(query)
            time.sleep(3)
            py.press('enter')

        elif 'pause' in query:
            py.press('space')

        elif "close it" in query:
            py.hotkey("alt", "f4")

        elif 'go offline' in query :
            main_file.end()
        
        else:
            main_file.main(query)
