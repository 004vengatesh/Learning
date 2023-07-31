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
