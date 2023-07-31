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
