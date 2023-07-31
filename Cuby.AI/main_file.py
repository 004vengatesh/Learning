import command_speak 
import pywhatkit
import pyautogui as py
import time
import startup_file
import os
import chatbot
import main_file_2

def end():
    command_speak.speak("thank you... please visit again !")
    startup_file.startup()

def main():
    command_speak.speak('listening....')
    while True:
        query = command_speak.takecommandexceptional(7)
        query =query.lower()
        
        chat = chatbot.chatbot(query)
        
        
        #query = textinput()
        if 'time' in query :
            startup_file.curtime()
        elif 'date' in query:
            startup_file.date()
        elif 'write a long note about' in query:
            query_1 = query.replace('write a long note about','')
            query = pywhatkit.info(query_1, 10, True)
            py.click(200,800)
            time.sleep(5)
            py.write('notepad')
            time.sleep(3)
            py.press('enter')
            time.sleep(6)
            py.write(query)

        elif 'what is' in query:
            query = query.replace('what is','')
            quest = pywhatkit.info(query, 2, True)
            command_speak.speak(quest)
        
        elif 'tell me about' in query:
            query = query.replace('tell me about','')
            quest = pywhatkit.info(query, 2, True)
            command_speak.speak(quest)
        
        elif 'define' in query:
            query = query.replace('define','')
            quest = pywhatkit.info(query, 2, True)
            command_speak.speak(quest)
        elif'wikipedia'in query:
            command_speak.speak('what should i search?')
            query = command_speak.takecommandexceptional(6)
            quest = pywhatkit.info(query, 3, True)
            command_speak.speak(quest)
        elif 'make a search about' in query:
            search = query.replace('make a search about','')
            pywhatkit.search(search)
        elif 'log out my pc' in query:
            command_speak.speak('warning! it will lock your system. please confirm the command, say yes to continue')
            lock = command_speak.takecommandexceptional(5)
            if 'yes' in lock:
                os.system('C:\\Windows\\System32\\rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
            else:
                command_speak.speakinput()
        elif 'shut down my pc' in query:
            command_speak.speak('warning! it will shutdown your system. please confirm the command, say yes to continue')
            lock = command_speak.takecommandexceptional(5)
            if 'yes' in lock:
                os.system('C:\\Windows\\System32\\shutdown.exe /s /t 0')
            else:
                command_speak.speakinput()
        else:
            main_file_2.main_2(query,query_1)
