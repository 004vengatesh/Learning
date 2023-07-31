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
