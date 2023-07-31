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
