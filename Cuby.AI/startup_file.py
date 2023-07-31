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


