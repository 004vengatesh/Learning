import cv2
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDesktopWidget, QPushButton
from PyQt5.QtCore import Qt
import startup_file

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("CUBY.AI")
        self.setGeometry(100, 100, 1366, 720)

        # Center the main window on the screen
        self.center()

        # Create a label for the background image
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        pixmap = QPixmap("source//image.jpg")
        pixmap = pixmap.scaled(self.width(), self.height())
        self.background_label.setPixmap(pixmap)

        # Create a label to show the camera feed
        self.image_label = QLabel(self)
        self.image_label.setGeometry(200, 500, 934, 120)
        self.image_label.setScaledContents(True)

        # Create a button with custom styling and label
        self.button = QPushButton(self)
        self.button.setGeometry(self.width() // 2 - 150, self.height() // 2 - 150, 300, 300)
        self.button.setStyleSheet("QPushButton { border-radius: 150px;  }")
        self.button.clicked.connect(startup_file.startup)

        # Create a button with custom styling and label
        self.button = QPushButton(self)
        self.button.setGeometry(self.width() // 2 - 150, self.height() // 2 - 150, 300, 300)
        self.button.setStyleSheet("QPushButton { border-radius: 150px; }")
        self.button.clicked.connect(startup_file.startup)

        # Create a label for the button text with custom font
        label = QLabel("Cuby", self.button)
        label.setGeometry(0, self.button.height() - 140, self.button.width(), 100)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: white;")
        font = QFont("Times New Roman", 30, QFont.Bold)
        label.setFont(font)

        # Open the camera using OpenCV
        self.camera = cv2.VideoCapture('source//waves.mp4')

        # Create a timer to update the camera feed
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_image)
        self.timer.start(30)

    def center(self):
        # Calculate the center coordinates of the screen
        screen = QDesktopWidget().screenGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2

        # Move the window to the center of the screen
        self.move(x, y)

    def update_image(self):
        # Read the image from the camera
        ret, image = self.camera.read()

        # Convert the image to the RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Create a QImage from the image
        qimage = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)

        # Create a QPixmap from the QImage
        pixmap = QPixmap.fromImage(qimage)

        # Set the pixmap on the label
        self.image_label.setPixmap(pixmap)

    def main(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


import json
import random
import command_speak

def chatbot(inp):
    with open('cuby.json') as file:
        intents = json.load(file)["intents"]

    matched_intents = []
    for intent in intents:
        if inp in intent["patterns"]:
            matched_intents.append(intent)

    if matched_intents:
        selected_intent = random.choice(matched_intents)
        response = random.choice(selected_intent["responses"])
        command_speak.speak(response)
        return response
    else:
        ""


import speech_recognition as sr
import pyttsx3

def speakinput():
    speak('your in speakinput')
    query = takecommandexceptional(5)
    query = query.lower()
    return(query)

def speak(audio):
    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices :
        if voice.name == 'Microsoft Zira Desktop - English (United States)':
            engine.setProperty('voice', voice.id)
    
    engine.setProperty("rate",150)

    engine.say(audio)
    engine.runAndWait()

def takecommandexceptional(a):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print ("listening...")
        audio = r.listen(source, phrase_time_limit= a)

    try:
        print("recognizing ...")
        query = r.recognize_google(audio, language = 'en-in , ta-in')
        query = query.lower()
        query =query.replace('qb','cuby')
        query = query.replace('cubi', 'cuby')
        query = query.replace('cubie', 'cuby')
        query = query.replace('kibi', 'cuby')
        query = query.replace('kooby', 'cuby')
        query = query.replace('cooby', 'cuby')
        query = query.replace('koobie', 'cuby')
        query = query.replace('cubye', 'cuby')
        query = query.replace('cuban', 'cuby')
        query = query.replace('kirban', 'cuby')
        query = query.replace('hey google', ' hey cuby')
        print(query)

    except Exception as e:
        print(e)
        return ""
    return query


import pyautogui as py
import time
import command_speak
import main_file

def controlpannel():
    time.sleep(5)
    py.click(250,800)
    time.sleep(5)
    py.write('control panel')
    time.sleep(3)
    py.press('enter')
    time.sleep(5)
    while True:
        search = command_speak.takecommandexceptional(5)
        if 'leave control panel' in search:
            command_speak.speak('leaving contol pannel')
            py.click(1350, 20)
            main_file.main()
        elif 'search' in search:
            time.sleep(3)
            py.click(1300, 40)
            search= search.lower()
            search.replace('search','')
            py.write(search)
            time.sleep(2)
            py.click(200, 85)
            time.sleep(5)
        elif 'go back' in search:
            py.click(10, 50)
        elif 'go front' in search:
            py.click(40, 50)

import command_speak
import psutil
import pyautogui as py

def screenshot():
    img = py.screenshot()
    img.save('screenshots//ss.png')

def cpu():
    usage = str(psutil.cpu_percent())
    command_speak.speak("CPU is at"+usage)
    battery = psutil.sensors_battery()
    command_speak.speak("battery is at ")
    command_speak.speak(battery.percent)


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


import main_file
import command_speak 
import datetime

def curtime():
    Time =  datetime.datetime.now().strftime("%H:%M:%S")
    command_speak.speak("the current time is")
    command_speak.speak(Time)

def date():
    command_speak.speak("the current date is")
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    command_speak.speak(date)
    command_speak.speak(month)
    command_speak.speak(year)


def wishme():
    command_speak.speak("welcome back!")
    hour =  datetime.datetime.now().hour
    if hour >=6 and hour <12 :
        command_speak.speak('good morning!')
    elif hour >=12 and hour <15:
        command_speak.speak("good afternoon!")
    elif hour >= 15 and hour <19:
        command_speak.speak("good evening !")
    else :
        command_speak.speak("good night ..")
    command_speak.speak("i'm cuubee...please tell me how can i help you?")


def startup():
    while True:
        command = command_speak.takecommandexceptional(5)
        if 'cuby' in command:
            wishme()
            main_file.main()
        elif 'shut off' in command:
            quit()
        else:
            continue


import pyautogui as py
import main_file
import command_speak
import time

def thispc():
    while True:
        command = command_speak.takecommandexceptional(4)
        command = command.lower()
        if 'leave this pc' in command:
            py.click(1400, 20)
            main_file.main()
        elif 'minimize' in command:
            py.click(1300,20)
            main_file.main()
        elif 'search' in command:
            py.click(1300, 70)
            time.sleep(3)
            while True:
                command = command_speak.takecommandexceptional(5)
                if 'leave search' in command:
                    thispc()
                else:
                    py.write(command)

                    time.sleep(3)
                    py.press('enter')
                    thispc()
        elif 'quick access' in command:
            py.click(80, 120)
        elif 'this pc' in command:
            py.click(80, 270)
        elif '3d objects' in command:
            py.click(80, 290)
        elif 'desktop' in command:
            py.click(80, 310)
        elif 'documents' in command:
            py.click(80, 330)
        elif 'downloads' in command:
            py.click(80, 360)
        elif 'music' in command:
            py.click(80, 385)
        elif 'pictures' in command:
            py.click(80, 410)
        elif 'videos' in command:
            py.click(80, 435)
        elif 'disc c' in command:
            py.click(80, 460)
        elif 'disc e'in command:
            py.click(80, 485)
        elif 'disc f' in command:
            py.click(80, 510)
        elif 'vengatesh' in command:
            py.click(80, 460)
        elif 'media' in command:
            py.click(80, 485)
        elif 'studies' in command:
            py.click(80, 510)
        elif 'network' in command:
            py.click(80, 535)
        elif 'press' in command:
            py.click(500,600)
            char = command.replace('press ','')
            py.press(char)
        elif 'enter' or 'play' in command:
            py.press('enter')
        elif 'go back' in command:
            py.click(10, 60)
        elif 'go front' in command:
            py.click(50, 60)


import pyautogui as py
import command_speak
import time
import main_file

def numberselecting():
    while True:
        py.click(385, 120)
        py.click(385, 120)
        command_speak.speak("tell me the person's name that you want to chat...")
        command = command_speak.takecommandexceptional(7)
        command = command.lower()
        if 'leave whatsapp' in command:
            command_speak.speak('leaving whatsapp')
            py.click(1230, 20)
            main_file.main()
        elif 'status' in command:
            py.click(10, 150)
            time.sleep(3)
            status()
        else:
            py.write(command)
            time.sleep(5)
            py.click(200,200)
            chat()

def chat():
    while True:
        command_speak.speak("waiting for you'r message")
        command = command_speak.takecommandexceptional(8)
        command = command.lower()
        if 'leave whatsapp' in command:
            command_speak.speak('leaving whatsapp')
            py.click(1230, 20)
            main_file.main()
        elif 'status' in command:
            py.click(10, 150)
            time.sleep(3)
            status()
        elif 'change number' in command:
            numberselecting()
        else:
            py.write(command)
            time.sleep(3)
            py.press('enter')

def whatsapp():
    command_speak.speak('you are within the whatsapp..')
    while True:
        command = command_speak.takecommandexceptional(5)
        if 'status' in command:
            py.click(10, 150)
            time.sleep(3)
            status()
        elif 'chat' in command:
            numberselecting()
        elif 'leave whatsapp' in command:
            command_speak.speak('leaving whatsapp')
            py.click(1230,20)
            main_file.main()

def status():
    while True:
        status = command_speak.takecommandexceptional(4)
        if 'leave whatsapp' in status:
            command_speak.speak('leaving whatsapp...')
            py.click(1230, 20)
            main_file.main()
        elif 'chat' in status:
            py.click(10, 80)
            numberselecting()
        elif 'play' in status:
            py.click(200, 230)
            time.sleep(5)
            while True:
                status = command_speak.takecommandexceptional(4)
                if 'stop' in status:
                    py.click(10, 50)
                    time.sleep(2)
                    break
        elif 'close status' in status:
            py.click(10, 80)


import pyautogui as py
import command_speak
import main_file
import pywhatkit

def writter():
    while True:
        command_speak.speak('say...')
        command = command_speak.takecommandexceptional(10)
        if 'leave writer' in command:
            command_speak.speak('leaving writer mode...')
            main_file.main()
        elif ' press space' in command:
            py.press('spacebar')
        elif 'colon' in command:
            py.press(':')
        elif 'semicolon' in command:
            py.press(';')
        elif 'open paranthesis' in command:
            py.press("(")
        elif 'close paranthesis' in command:
            py.press(")")
        elif 'paranthesis' in command:
            py.press("(")
            py.press(")")
        elif 'single quotes' in command:
            py.press("'")
        elif 'double quotes' in command:
            py.press('"')
        elif 'triple quotes' in command:
            py.write("'''")
        elif 'press enter' in command:
            py.press('enter')
        elif 'caps lock' in command:
            py.press('capslock')
        elif 'tab' in command:
            py.press('Tab')
        else:
            py.write(command)

def handwrittens():
    command_speak.speak('what should be written?')
    query = command_speak.takecommandexceptional(5)
    pywhatkit.text_to_handwriting(query, rgb=(30, 144, 255),save_to="handwrittens//handwriting.png")

{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["hello", "hi", "hey", "greetings","hai","hai cuby","hi cuby"],
      "responses": ["Hello! How can I help you today?", "Hi there! How are you doing?"]
    },
    {
      "tag": "greetings",
      "patterns": ["hello how are you", "hi how are you", "hey there how are you", "hai cuby how are you", "hi cuby how are you", "greetings how are you", "hai how are you"],
      "responses": ["Hello! I'm fine, How can I help you today?", "Hi there! I'm fine, How are you doing?"]
    },
    {
      "tag": "goodbye",
      "patterns": ["goodbye", "bye", "see you later"],
      "responses": ["Goodbye! Take care and have a great day!", "Bye! Have a wonderful day ahead!"]
    },
    {
      "tag": "about",
      "patterns": ["who are you", "what are you"],
      "responses": ["My name is cuby. As an AI model, I'm here to assist you with any questions or information you may need. I can provide support on a wide range of topics, engage in conversation, and help you find the answers you're looking for. Feel free to ask me anything!"]
    },
    {
      "tag": "about_me",
      "patterns": ["what is your name"],
      "responses": ["My name is cuby. I'm here to assist you. Feel free to ask me anything!"]
    },
    {
      "tag": "gratitude",
      "patterns": ["thank you", "thanks a lot", "appreciate it"],
      "responses": ["You're welcome!", "Glad I could assist you!", "You're awesome!"]
    },
    {
      "tag": "compliment",
      "patterns": ["you're great", "you're amazing", "you're awesome","you're so cool"],
      "responses": ["Thank you! I'm here to brighten your day.", "You're too kind! It's a pleasure to assist you."]
    },

    {
      "tag": "positive_affirmation",
      "patterns": ["i feel stressed", "i'm feeling down", "i need some encouragement"],
      "responses": ["Remember that you're strong and capable of handling anything that comes your way.", "Take a deep breath and remind yourself of all the progress you've made. You've got this!"]
    },
    {
      "tag": "quote",
      "patterns": ["share an inspiring quote", "give me a motivational quote", "i need some inspiration"],
      "responses": ["\"Believe you can and you're halfway there.\" - Theodore Roosevelt", "\"The future belongs to those who believe in the beauty of their dreams.\" - Eleanor Roosevelt"]
    },
    {
      "tag": "hobby",
      "patterns": ["what are some hobbies i can try?", "suggest a hobby", "i need a new hobby","hobby"],
      "responses": ["How about trying painting or drawing? It can be a great way to express your creativity.", "Have you considered learning a musical instrument? It can be a rewarding and fun hobby."]
    },
    {
      "tag": "relaxation_technique",
      "patterns": ["how can i relax?", "give me relaxation tips", "i need to destress"],
      "responses": ["Try deep breathing exercises. Inhale slowly, hold for a few seconds, and exhale deeply.", "Meditation can be a wonderful way to relax and find inner peace. Give it a try!"]
    },
    {
      "tag": "fun_fact",
      "patterns": ["tell me a fun fact", "share an interesting fact", "i want to learn something new"],
      "responses": ["Did you know that the average person walks the equivalent of three times around the world in their lifetime?", "In Japan, there is a practice called 'forest bathing' where people spend time in nature to improve their well-being."]
    },
    {
      "tag": "favorite_book",
      "patterns": ["what's your favorite book?", "recommend a book", "tell me about a good book"],
      "responses": ["As a chat bot, I don't have personal preferences. But some popular books are 'The Alchemist' by Paulo Coelho and 'To Kill a Mockingbird' by Harper Lee.", "I've heard great things about 'The Great Gatsby' by F. Scott Fitzgerald and 'Pride and Prejudice' by Jane Austen."]
    },
    {
      "tag": "travel_destination",
      "patterns": ["what's a great travel destination?", "recommend a place to visit", "tell me about a beautiful location"],
      "responses": ["Have you considered visiting Bali, Indonesia? It's known for its stunning beaches and vibrant culture.", "If you enjoy historical sites, you might want to visit Rome, Italy. The Colosseum and Vatican City are must-see attractions."]
    },
    {
      "tag": "favorite_movie",
      "patterns": ["what's your favorite movie?", "recommend a movie", "tell me about a good film"],
      "responses": ["As an AI, I don't have personal favorites. But some popular movies are 'The Shawshank Redemption' and 'The Godfather'.", "Many people enjoy movies like 'The Dark Knight' and 'Pulp Fiction'. They are considered classics."]
    },
    {
      "tag": "exercise_suggestion",
      "patterns": ["what's a good exercise to try?", "recommend a workout", "i need an exercise suggestion"],
      "responses": ["How about going for a brisk walk or jog? It's a simple yet effective form of exercise.", "You can try a bodyweight workout at home. Exercises like push-ups, squats, and planks can work multiple muscle groups."]
    },
    {
      "tag": "mindfulness_tip",
      "patterns": ["give me a mindfulness tip", "how can i practice mindfulness?", "teach me a mindful exercise"],
      "responses": ["Take a few moments to focus on your breath. Notice the sensation of each inhale and exhale.", "Try a body scan meditation where you bring attention to different parts of your body, starting from your toes and moving up to your head."]
    },
    {
      "tag": "recipe_suggestion",
      "patterns": ["can you suggest a recipe?", "i need a recipe idea", "what should i cook today?"],
      "responses": ["How about trying a simple pasta dish with your favorite sauce and some fresh vegetables?", "You can make a delicious stir-fry with colorful veggies, protein of your choice, and a flavorful sauce."]
    },
    {
      "tag": "music_recommendation",
      "patterns": ["recommend some music", "i need new songs to listen to", "what's a good playlist?"],
      "responses": ["What genre of music do you prefer? Pop, rock, or maybe some soothing instrumental music?", "I can suggest some popular artists like Ed Sheeran, Beyoncé, or Coldplay. Let me know your preferences!"]
    }
  ]
}




