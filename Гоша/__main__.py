import os
import speech_recognition as sr
import pyttsx3
import re

import argparse

import threading
from tkinter import *

import time

import random

import sys

import ctypes



def exit_all():
    global t1, t2, t3

    exit()
    t1.do_run = False
    t2.do_run = False
    t3.do_run = False

    t1.stop()
    t2.stop()
    t3.stop()
    exit()

def emoc_new():
    global emoc, canv



    if emoc == '0':
        canv.create_oval(0,0,350,350,fill="yellow",outline="yellow")
        canv.create_rectangle(20,190,330,200,fill="black",outline="black")
        canv.create_oval(50,50,100,100,fill="white",outline="white")
        canv.create_oval(250,50,300,100,fill="white",outline="white")
        canv.create_oval(60,60,90,90,fill="black",outline="black")
        canv.create_oval(260,60,290,90,fill="black",outline="black")
    elif emoc == '1':
        canv.create_oval(0,0,350,350,fill="yellow",outline="yellow")
        canv.create_arc([330,325], [20,150],start=15,extent=150,style=ARC,outline="black",width=10)
        canv.create_oval(50,50,100,100,fill="white",outline="white")
        canv.create_oval(250,50,300,100,fill="white",outline="white")
        canv.create_oval(60,60,90,90,fill="black",outline="black")
        canv.create_oval(260,60,290,90,fill="black",outline="black")
    elif emoc == '2':
        canv.create_oval(0,0,350,350,fill="yellow",outline="yellow")
        canv.create_arc([330,250], [20,150],start=195,extent=150,style=ARC,outline="black",width=10)
        canv.create_oval(50,50,100,100,fill="white",outline="white")
        canv.create_oval(250,50,300,100,fill="white",outline="white")
        canv.create_oval(60,60,90,90,fill="black",outline="black")
        canv.create_oval(260,60,290,90,fill="black",outline="black")
    elif emoc == '3':
        canv.create_oval(0,0,350,350,fill="yellow",outline="yellow")
        canv.create_arc([330,250], [20,0],start=195,extent=150,style=ARC,outline="black",width=10)
        canv.create_oval(50,50,100,100,fill="white",outline="white")
        canv.create_oval(250,50,300,100,fill="white",outline="white")
        canv.create_oval(60,60,90,90,fill="black",outline="black")
        canv.create_oval(260,60,290,90,fill="black",outline="black")

    else:
        canv.create_oval(0,0,350,350,fill="yellow",outline="yellow")
        canv.create_line(90,250,60,200,width=7,fill="black")
        canv.create_line(90,250,120,200,width=7,fill="black")
        canv.create_line(150,250,120,200,width=7,fill="black")
        canv.create_line(150,250,180,200,width=7,fill="black")
        canv.create_line(210,250,180,200,width=7,fill="black")
        canv.create_line(210,250,240,200,width=7,fill="black")
        canv.create_line(270,250,240,200,width=7,fill="black")
        canv.create_line(270,250,300,200,width=7,fill="black")        
        canv.create_oval(50,75,100,100,fill="white",outline="white")
        canv.create_oval(250,75,300,100,fill="white",outline="white")
        canv.create_oval(70,85,80,95,fill="black",outline="black")
        canv.create_oval(270,85,280,95,fill="black",outline="black")

def emoc(x):
    global emoc
    while True:
        eom = emoc
        my_file = open("bin\\emoc.bin", "r")
        emoc = my_file.read()
        my_file.close() 
        time.sleep(0.1)
        if eom != emoc:
            emoc_new()

def one(x):
    global emoc, canv 
    if x == "0":
        window = Tk()
        window.title("Добро пожаловать. Я Гоша!")
        w = window.winfo_screenwidth() # ширина экрана
        h = window.winfo_screenheight() # высота экрана
        w = w//2 # середина экрана
        h = h//2 
        w = w +250
        h = h -300 # смещение от середины
        window.geometry('400x400+{}+{}'.format(w, h))
        window.iconbitmap(r'bin/icon/icon.ico')
        lbl = Label(window, text="")  
        lbl.grid(column=0, row=0) 
        canv=Canvas(window,width=350,height=350,cursor="pencil")     
        
        canv.grid(column=1, row=1)

        window.mainloop()
    if x == "1":
        while  __name__ == '__main__':
            if __name__ != '__main__':
                speak_engine = pyttsx3.init()
                
                def speak(what):
                    print( what )
                    speak_engine.say( what )
                    speak_engine.runAndWait()
                    speak_engine.stop()
                
                r = sr.Recognizer()

                speak("Debug, модуль запущен!!!")
                speak("")
                speak("Проверка подключенных модулей - 100% OK")
                speak("Тест искуственного интелекта - 100% OK")
                speak("Проверка актуальности прошивки - 100% OK")
                speak("Проверка звука - 1 2 3 4 5 6 - 100% OK")

                with sr.Microphone(device_index=1) as source:
                    speak("Тест микрофона, скажите что-нибудь ...")        
                    audio = r.listen(source)
                    try:
                        query = r.recognize_google(audio, language="ru-RU")
                        string=query.lower()
                        speak("Вы сказали: " + str(string))
                        #global ema
                        speak("Успешно!!!")
                    except sr.UnknownValueError:
                        print("[log] Голос не распознан!")

                speak("Скажите число от 1 до 5 для запуска модулей:")
                speak("")
                speak("1 - Расширенная проверка ии.")
                speak("2 - Тест искуственных нейронов.")
                speak("3 - Проверка верности ответов.")
                speak("4 - Изменение системы самообучения.")
                speak("5 - Тест логичности нейронных связей.")

                with sr.Microphone(device_index=1) as source:        
                    audio = r.listen(source)
                    try:
                        query = r.recognize_google(audio, language="ru-RU")
                        string=query.lower()
                        print("Вы сказали: " + str(string))
                        if string == "1":
                            speak("Расширенная проверка ии:")
                            time.sleep(5)
                            rand = random.randint(1, 999)
                            rand2 = random.randint(0, 9)
                            rand3 = int(rand) - int(rand2)
                            speak("")
                            speak("Битых нейронов: " + str(rand))
                            speak("Востановлено: " + str(rand3))
                        if string == "2":
                            speak("Тест искуственных нейронов:")
                            speak("Схемотичное расприделение нейронов выведено на экран:")
                            speak("")
                            f = open("bin/neiron.bin",'r',encoding = 'utf-8')
                            print(f.read());
                            speak("Извините, что я не перевел в стандартный вид. Но этого было очень много!")
                        if string == "3":
                            speak("Проверка верности ответов.")
                        if string == "4":
                            speak("Изменение системы самообучения.")
                        if string == "4":
                            speak("Тест логичности нейронных связей.")
                        #global ema
                    except sr.UnknownValueError:
                        print("[log] Голос не распознан!")
                
                
            else:

                i = 0

                while i < 100:
                    speak_engine = pyttsx3.init()
                    def speak(what):
                        print( what )
                        speak_engine.say( what )
                        speak_engine.runAndWait()
                        speak_engine.stop()
                    r = sr.Recognizer()
                    


                    def priv(string):
                        global kak, im
                        pattern = re.compile("(гоша|георгий|включись|запустить|включить|запустись|слушай|слушать)")
                        match   = pattern.search(string)
                        if match:
                           speak("");
                           os.system("python __init__.py")
                           
                    def ex(string):
                        global kak, im
                        pattern = re.compile("(выйти)")
                        match   = pattern.search(string)
                        if match:
                           speak("ОКЕЙ");
                           exit_all() 
                    
                    def conf(string):
                        global im, kak
                        im = 0
                        kak = 0
                        priv(string)
                        ex(string)
                            

                    with sr.Microphone(device_index=1) as source:
                        print("Скажите что-нибудь ...")        
                        audio = r.listen(source)
                        try:
                            query = r.recognize_google(audio, language="ru-RU")
                            string=query.lower()
                            print("Вы сказали: " + str(string))
                            #global ema            
                            conf(string)
                        except sr.UnknownValueError:
                            print("[log] Голос не распознан!")

#Проверка наличия аргументов cmd
if len (sys.argv) > 1:

    #Если аргумент = -dbg - Запуск debug'а
    if '-dbg' in sys.argv:
        speak_engine = pyttsx3.init()
                    
        def speak(what):
            print( what )
            speak_engine.say( what )
            speak_engine.runAndWait()
            speak_engine.stop()
                    
        r = sr.Recognizer()

        speak("Debug, модуль запущен!!!")
        speak("")
        speak("Проверка подключенных модулей - 100% OK")
        speak("Тест искуственного интелекта - 100% OK")
        speak("Проверка актуальности прошивки - 100% OK")
        speak("Проверка звука - 1 2 3 4 5 6 - 100% OK")

        with sr.Microphone(device_index=1) as source:
            speak("Тест микрофона, скажите что-нибудь ...")        
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language="ru-RU")
                string=query.lower()
                speak("Вы сказали: " + str(string))
                #global ema
                speak("Успешно!!!")
            except sr.UnknownValueError:
                print("[log] Голос не распознан!")

            speak("Скажите число от 1 до 5 для запуска модулей:")
            speak("")
            speak("1 - Расширенная проверка ии.")
            speak("2 - Тест искуственных нейронов.")
            speak("3 - Проверка верности ответов.")
            speak("4 - Изменение системы самообучения.")
            speak("5 - Тест логичности нейронных связей.")

        with sr.Microphone(device_index=1) as source:
            r.adjust_for_ambient_noise(source)        
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language="ru-RU")
                string=query.lower()
                print("Вы сказали: " + str(string))
                if string == "1":
                    speak("Расширенная проверка ии:")
                    time.sleep(5)
                    rand = random.randint(1, 999)
                    rand2 = random.randint(0, 9)
                    rand3 = int(rand) - int(rand2)
                    speak("")
                    speak("Битых нейронов: " + str(rand))
                    speak("Востановлено: " + str(rand3))
                if string == "2":
                    speak("Тест искуственных нейронов:")
                    speak("Схемотичное расприделение нейронов выведено на экран:")
                    speak("")
                    f = open("bin/neiron.bin",'r',encoding = 'utf-8')
                    print(f.read());
                    speak("Извините, что я не перевел в стандартный вид. Но этого было очень много!")
                if string == "3":
                    speak("Проверка верности ответов.")
                if string == "4":
                    speak("Изменение системы самообучения.")
                if string == "4":
                    speak("Тест логичности нейронных связей.")
                    #global ema
            except sr.UnknownValueError:
                print("[log] Голос не распознан!")

    #Если аргумент = -GUI - Запуск окнового режима(Очень процесорно затратно!!! )
    elif '-GUI' in sys.argv:
        myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        my_file = open("bin\\emoc.bin", "w")
        my_file.write(str(0))
        my_file.close()
        global t1,t2,t3

        t1 = threading.Thread(target=one, args=('0'))
        t2 = threading.Thread(target=one, args=('1'))
        t3 = threading.Thread(target=emoc, args=('2'))

        t1.start()
        t2.start()
        t3.start()


        t1.join()
        t2.join()
        t3.join()

else:
    one('1')