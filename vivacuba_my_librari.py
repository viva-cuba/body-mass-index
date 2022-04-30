

import os
import playsound
import speech_recognition as sr
from gtts import gTTS
import random


# принимает голосовую команду
def listen_command() -> None:
    """принимает голосовую команду"""
# пример написания и обращение к модулю
    """from vivacuba_my_librari import listen_command as lk, say_message

    def mess(message):
        if "привет" in message:
            say_message('привет, привет')
        elif 'как дела' in message:
            say_message('нормально')
        elif 'выход' in message:
            exit()  
    while True: 
        message = lk()
        mess(message)"""
# или так...один запрос, один ответ
    """from vivacuba_my_librari import listen_command as lk, say_message

    message = lk()
    if 'привет' in message:
        say_message('упссс а ты кто?')"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("слушаю тебя:")  
        new_func(r, source)
        audio = r.listen(source)
        print('услышала: ')
    try:
        our_speech = r.recognize_google(audio, language="ru-RU").lower()
        print("вы сказали: " + our_speech)
        return our_speech
    except sr.UnknownValueError:
        return("ошибка")
    except sr.RequestError as e:
        print(e)
    except ConnectionError as e:
        print(e)

def new_func(r, source):
    r.adjust_for_ambient_noise(source, duration=1)
    r.pause_threshold = 1    
               
# озвучивает строку
def say_message(message: str) -> None:
    """ПРИМЕР
    from vivacuba_my_librari import say_message
    say_message('привет, как дела')

    озвучивает строку"""
    try:
        voice = gTTS(message, lang="ru")
        file_voice_name = "_audio_"+ str(random.randint(0, 10000)) +".mp3"
        voice.save(file_voice_name)
        playsound.playsound(file_voice_name)
        os.remove(file_voice_name)
        print("Маруся: "+message)
    except sr.RequestError as e:
        print(e)
    except TimeoutError:
        return 'ошибка' 

