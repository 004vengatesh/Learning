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

