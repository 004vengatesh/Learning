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
