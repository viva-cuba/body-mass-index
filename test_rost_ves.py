# win 7 64 bit//python 3.7.6//vivacuba
# программа для вычисления соотношения массы и роста. чисто поиграться...
# "ИНДЕКС МАССЫ ТЕЛА:  величина, позволяющая оценить степень соответствия массы человека
#  и его роста и тем самым косвенно судить о том, является ли масса недостаточной,
#  нормальной или избыточной. Важен при определении показаний для необходимости лечения.

import os
from gtts import gTTS
import random
import time
import playsound
import speech_recognition as sr

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        print("слушаю тебя:")
        audio = r.listen(source)   
    try:
        our_speech = r.recognize_google(audio, language="ru-RU")
        print("вы сказали: "+our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError as e:
        return "ошибка"
    
def do_tris_command(message):
    message = message.lower()
    names = name

    if "давай" in message:
        say_message('ну что ' + names + ' начнём, скажи свой рост. например 180 сантиметров или 175 сантиметров 100 миллиметров, но я думаю миллиметров не надо, они сильно не повлияют на результат. говори')
        rost = float(listen_command().replace("см", '').replace('мм', '').strip().replace('  ', '.'))
        rost = rost/100
        say_message('хорошо ' + names + ' теперь вес.  например 71 килограмм или 85 килограмм 400 грамм. говори')
        wes = float(listen_command().replace("кг", '').replace('г', '').replace('грамм', '').strip().replace('  ', '.'))
        say_message('хорошо')
        bmi = (wes/(rost ** 2))
        print(bmi)

        if bmi >= 10 and bmi <= 18.49:
            say_message(names + " у Вас дефицит массы тела, нужно больше кушать, витамины там всякие, фрукты, овощи, ну и мясо наконец")
            say_message(names + " была ли информация полезна для вас?")
        elif bmi >= 18.5 and bmi <= 24.9:
            say_message(names + " У Вас нормальная масса тела, ПОЗДРАВЛЯЮ! В здоровом теле, здоровый дух")
            say_message(names + " была ли информация полезна для вас?")
        elif bmi >= 25 and bmi <= 29.9:
            say_message(names + " У вас избыточная масса тела, похоже после 6ти вечера кушать не стоит")
            say_message(names + " была ли информация полезна для вас?")
        elif bmi >= 30 and bmi <= 34.9:
            say_message(names + " у вас ожирение первой степени: Ну, что сказать, холодильник на сигнализацию и включить сирену")
            say_message(names + " была ли информация полезна для вас?")
        elif bmi >= 35 and bmi <= 39.9:
            say_message(names + " У вас ожирение второй степени: похоже нужно обратиться к врачу, со здоровьем не шутят")
            say_message(names + " была ли информация полезна для вас?")
        elif bmi >= 40:
            say_message(names + " У вас ожирение третьей степени: без комментариев, только к врачу")
            say_message(names + " была ли информация полезна для вас?")

    elif "пока" in message:
        say_message('будь здоров')
        exit()  

    elif "нет" in message:
        say_message('ну извини я только результат сказала, а о своём здоровье '  + names +  ' ты должен сам заботиться')
        exit()

    elif "да" in message:
        say_message("рада была помочь")
        exit()

    else:
        say_message("я очень рада что смогла вам помочь")
        exit()

def say_message(message):
    
    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_" + \
    str(time.time())+"_"+str(random.randint(0, 100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    os.remove(file_voice_name)
    print("Голосовой ассистент: "+message)

if __name__ == '__main__':
    say_message("ИНДЕКС МАССЫ ТЕЛА:  величина, позволяющая оценить степень соответствия массы человека и его роста\n и тем самым косвенно судить о том, является ли масса недостаточной, нормальной или избыточной.\n Важен при определении показаний для необходимости лечения:")
    
    say_message('как тебя зовут:')
    name = listen_command()
    say_message('привет ' + name + ' давай посчитаем? если хочешь продолжить, то скажи давай, если нет скажи пока. ну что приступим?')

    while True:
        command = listen_command()
        do_tris_command(command)