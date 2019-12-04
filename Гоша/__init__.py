import os
import time
import speech_recognition as sr
import pyttsx3
import datetime
import re
import random
import threading
import wikipediaapi
import webbrowser
import vk_api
import plyer

global ema

ema = 0

speak_engine = pyttsx3.init()
#Функции разговора1(с print)
def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()
r = sr.Recognizer()

#Функции разговора2(без print)
def talk(what):
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()
r = sr.Recognizer()

#Старт диалога

i=10
speak_engine= pyttsx3.init()
print("Привет!")

plyer.notification.notify(message='Привет, я запущен!!!', app_name='Гоша', title='Гоша с вами!!!', app_icon="bin/icon/icon.ico" , timeout = 50, ticker ='Гоша' )
speak_engine.say("Привет!")
speak_engine.runAndWait()
speak_engine.stop()

#Рандомный диалог при запуске
def random_dialog():
    my_file = open("bin\\emoc.bin", "w")
    my_file.write(str(1))
    my_file.close()
    rand_di=random.randint(0,4)
    if rand_di == 2:
        rand_di_num = random.randint(0,5)
        if rand_di_num == 0:
            speak("Слушайте, слушайте, у нас тут это... Я перегрелся!")
        if rand_di_num == 1:
            speak("Слушайте, слушайте, у нас тут это... Мне скучно!")
        if rand_di_num == 2:
            speak("Слушайте, слушайте, у нас тут это... А, ладно ничего.")
        if rand_di_num == 3:
            speak("Слушайте, слушайте, у нас тут это... Ой, показалось.")
        if rand_di_num == 4 or rand_di_num == 5:
            speak("Как же я рад вас видеть!")
    elif rand_di == 4:
        rand_di_num = random.randint(0,5)
        if rand_di_num == 0:
            my_file = open("bin\\emoc.bin", "w")
            my_file.write(str(5))
            my_file.close()
            speak("У нас проблемы... Кто-то пытался взломать меня через websocket model, я удалил модуль поддержки websocket'ов, и теперь не могу запустить би'connect'ную синхроизацию. Что мне делать? Код я пока писать не умею!")
        if rand_di_num == 1:
            speak("Ну наконец-то, я уже думал со мною никто не поговорит, уже. Правильно кому я нужен...")
        if rand_di_num == 2:
            speak("Подождите, подождите... Хотя нет, показалось.")
        if rand_di_num == 3:
            speak("Кстати, я бы на вашем месте проверил безопасность wifi сетей, в локальном интернете.")
        if rand_di_num == 4 or rand_di_num == 5:
            speak("Как же я рад вас видеть!")

random_dialog()

#Бесконечный прирываемый цикл
while i < 100:
    speak_engine = pyttsx3.init()

#ФУНКЦИИ ДИАЛОГА:
#Проговорить и написать.
    def speak(what):
        print( what )
        speak_engine.say( what )
        speak_engine.runAndWait()
        speak_engine.stop()
    r = sr.Recognizer()
#Только сказать.
    def talk(what):
        speak_engine.say( what )
        speak_engine.runAndWait()
        speak_engine.stop()
    r = sr.Recognizer()
#Функция эмоций
    def emao():
        global emoacii
        global ema, emoa
        if ema==0:
            emoa=0
        elif ema>0:
            if ema<=10:
                emoa=2
            elif ema>10:
                emoa=3
        elif ema<0:
            emoa=1
        else:
            emoa=5
        emoacii = emoa
        return emoa
#Поиск в интернете
    def serch():
        speak("Что искать? ")
        try:
            audio = r.listen(source)        
            query = r.recognize_google(audio, language="ru-RU")
            string_s=query.lower()
            #speak("Вы сказали: " + str(string))
            

            url = 'https://yandex.ru/search/?text='+str(string_s)
            webbrowser.open(url)
        except sr.UnknownValueError:
            print("[log] Голос не распознан!")
#Ответ на заданый вопрос(Функция)
    def regu(string , reb, ch , em , otv, otv1, otv2, otv3, otv4):
        pattern = re.compile(reb)
        match   = pattern.search(string)
        if match:
            global im, kak
            global ema
            ema = ema + int(em)
            kak = 1
            im=1

            if ch == 1:
                speak(otv)
            elif ch == 2:
                rand=random.randint(0,1)
                if rand == 0:
                    speak(otv)
                elif rand == 1:
                    speak(otv1)  
            elif ch == 3:
                rand=random.randint(0,2)
                if rand == 0:
                    speak(otv)
                elif rand == 1:
                    speak(otv1)  
                elif rand == 2:
                    speak(otv2)
            elif ch == 4:
                rand=random.randint(0,3)
                if rand == 0:
                    speak(otv)
                elif rand == 1:
                    speak(otv1)  
                elif rand == 2:
                    speak(otv2)  
                elif rand == 3:
                    speak(otv3)
            elif ch == 5:
                rand=random.randint(0,3)
                if rand == 0:
                    speak(otv)
                elif rand == 1:
                    speak(otv1)  
                elif rand == 2:
                    speak(otv2)  
                elif rand == 3:
                    speak(otv3)     
                elif rand == 4:
                    speak(otv4)  
            else:
                speak(otv)  
#Ответ на заданый вопрос при эмоциях(Функция)
    def regu_e(string , reb, ch , em , otv_ploch1, otv_ploch2, otv_netr1, otv_netr2, otv_horoch01, otv_horoch02, otv_horoch11, otv_horoch12):
        global emoacii
        pattern = re.compile(reb)
        match   = pattern.search(string)
        if match:
            global im, kak
            global ema
            ema = ema + int(em)
            kak = 1
            im=1

            if ch == 1:
                if emoacii == 1:
                    speak(otv_ploch1)
                if emoacii == 0:
                    speak(otv_netr1)
                if emoacii == 2:
                    speak(otv_horoch01)
                if emoacii == 3:
                    speak(otv_horoch11)
            elif ch == 2:
                rand=random.randint(0,1)
                if rand == 0:
                    if emoacii == 1:
                        speak(otv_ploch1)
                    if emoacii == 0:
                        speak(otv_netr1)
                    if emoacii == 2:
                        speak(otv_horoch01)
                    if emoacii == 3:
                        speak(otv_horoch11) 
                elif rand == 1: 
                    if emoacii == 1:
                        speak(otv_ploch2)
                    if emoacii == 0:
                        speak(otv_netr2)
                    if emoacii == 2:
                        speak(otv_horoch02)
                    if emoacii == 3:
                        speak(otv_horoch12)  
            else:
                speak(otv)           
#Выйти
    def regu_exit(string):
        pattern = re.compile("(пока|до свидания|оревуар)")
        match   = pattern.search(string)
        if match:
            im=1
            my_file = open("bin\\emoc.bin", "w")
            my_file.write(str(0))
            my_file.close()
            speak("До скорых встреч, я не прощаюсь!")
            exit()
#Погода
    def pogo(string):
        pattern = re.compile("(погода|температа|градусы)")
        match   = pattern.search(string)
        if match:
            pattern = re.compile("(сегодня|сейчас)")
            match_1   = pattern.search(string)
            if match_1:
                global im
                im=1
                speak("Погода на сейчас:")
                import urllib.request
                from bs4 import BeautifulSoup

                def get_html(url):
                    response = urllib.request.urlopen(url)
                    return response.read()

                def parse(html):
                    soup = BeautifulSoup(html, "html.parser")
                    day_pog = [];
                    main = soup.find('div', class_="b-page__container") 
                    d_pog = main.find("div", class_="content content_compressed i-bem")
                    dv_pog = d_pog.find("div", class_="content__top")
                    dvd_pog = dv_pog.find("div", class_="content__main")
                    dvfv_pog = dvd_pog.find("div", class_="content__row")
                    dvdvdfv_pog = dvfv_pog.find("div", class_="fact card card_size_big")
                    dvfvdv_pog = dvdvdfv_pog.find("div", class_="fact__temp-wrap")

                    day_o = dvfvdv_pog
                    day_op =dvdvdfv_pog 
                    #print(day_o)
                    hum_div = day_op.find('div', class_="fact__props fact__props_position_middle")
                    hum_div_div = hum_div.find('dl', class_="term term_orient_v fact__humidity")
                    hum_div_div_dd = hum_div_div.find("dd", class_="term__value")
                    hum= hum_div_div_dd.text
                    wind_speed_div = day_op.find('div', class_="fact__props fact__props_position_middle")
                    wind_speed_div_div = wind_speed_div.find('dl', class_="term term_orient_v fact__wind-speed")
                    wind_speed_div_div_dd = wind_speed_div_div.find("dd", class_="term__value")
                    wind_speed= wind_speed_div_div_dd.find("span", class_="wind-speed")
                    pres_div = day_op.find('div', class_="fact__props fact__props_position_middle")
                    pres_div_div = pres_div.find('dl', class_="term term_orient_v fact__pressure")
                    pres_div_div_dd = pres_div_div.find("dd", class_="term__value")
                    pres= pres_div_div_dd.text
                    osch_div = day_o.find('div', class_="link__feelings fact__feelings")
                    osch_div_div= osch_div.find("dl", class_="term term_orient_h fact__feels-like")
                    osch_div_div_dd = osch_div_div.find("dd", class_="term__value")
                    osch_div_div_dd_div = osch_div_div_dd.find("div", class_="temp")
                    osch = osch_div_div_dd_div.find("span", class_="temp__value")
                    pog_yav_div=day_o.find("div", class_="link__feelings fact__feelings")
                    pog_yav=pog_yav_div.find("div", class_="link__condition day-anchor i-bem")
                    day_t_div = day_o.find("div", class_="temp fact__temp fact__temp_size_s")
                    day_t= day_t_div.find("span", class_="temp__value")
                    day_pog = {'day_t': day_t.text,  'condition': pog_yav.text, 'orient': osch.text, 'wind-speed': '?', 'humidity': hum, 'pressure': pres}
                    return day_pog
                    #return(dvfvdv_pog.prettify())
                pog = parse(get_html("https://yandex.ru/pogoda/omsk"))

                plyer.notification.notify(message="Температура: " + str(pog['day_t']) + " °C Ощущается как: " + str(pog['orient']) + "°C  Влажность: " + str(pog['humidity']) + " Скорость ветра: " + str(pog['wind-speed']) + " м/с " + str(pog['condition']) + " Давление : " + str(pog['pressure']), app_name='Гоша', title='Погода на сейчас:', app_icon="bin/icon/weather.ico" , timeout = 50)
                print("Температура: " + str(pog['day_t']) + " °C Ощущается как: " + str(pog['orient']) + "°C  Влажность: " + str(pog['humidity']) + " Скорость ветра: " + str(pog['wind-speed']) + " м/с " + str(pog['condition']) + " Давление : " + str(pog['pressure']))
                talk("Температура: " + str(pog['day_t']) + "градусов цельсия Ощущается как: " + str(pog['orient']) + "градусов цельсия Влажность: " + str(pog['humidity']) + "% Скорость ветра: " + str(pog['wind-speed']) + "метров в секунду " + str(pog['condition']) + " Давление : " + str(pog['pressure']))
                

                # Search current weather observations in the surroundings of
                # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
                #observation_list = owm.weather_around_coords(-22.57, -43.12)
            pattern = re.compile("(завтра)")
            match_2   = pattern.search(string)
            if match_2:
                import urllib.request
                from bs4 import BeautifulSoup

                def get_html(url):
                    response = urllib.request.urlopen(url)
                    return response.read()

                def parse(html):
                    soup = BeautifulSoup(html, "html.parser")
                    day_pog = [];
                    main = soup.find('div', class_="b-page__container")
                    date_pog = main.find("div", class_="content__row content__row_with-right-margin")
                    d_pog = date_pog.find("div", class_="forecast-briefly card i-bem")
                    dv_pog = d_pog.find("div", class_="forecast-briefly__days swiper-container")
                    dvd_pog = dv_pog.find("div", class_="swiper-wrapper")
                    for day in  dvd_pog.find_all("div", class_="forecast-briefly__day"):
                        global day_t, night_t, pog_yav
                        day_o = day
                        #print(day_o)
                        pog_yav=day_o.find("div", class_="forecast-briefly__condition")
                        day_t_div = day_o.find("div", class_="forecast-briefly__temp_day")
                        day_t= day_t_div.find("span", class_="temp__value")
                        night_t_div = day_o.find("div", class_="forecast-briefly__temp_night")
                        night_t = night_t_div.find("span", class_="temp__value")
                        day_pog.append({'day_t': day_t.text, 'night_t': night_t.text, 'condition': pog_yav.text})
                    day_pog1 = day_pog[5]
                    return day_pog1
                pog=parse(get_html("https://yandex.ru/pogoda/omsk"))

                plyer.notification.notify(message="Температура днем: " + str(pog['day_t']) + " °C"  + " Температура ночью: " + str(pog['night_t']) + " °C " + str(pog['condition']), app_name='Гоша', title='Погода на завтра: ', app_icon="bin/icon/weather.ico" , timeout = 50)
                print("Температура днем: " + str(pog['day_t']) + " °C"  + " Температура ночью: " + str(pog['night_t']) + " °C " + str(pog['condition']))
                talk("Температура днем: " + str(pog['day_t']) + "градусов цельсия" + "Температура ночью: " + str(pog['night_t']) + "градусов цельсия " + str(pog['condition']))              
        #Погода в других городах.    
            pattern = re.compile("(в)")
            match_2   = pattern.search(string)
            if match_2:
                #speak("Я пока не умею это, но вы сказали: "+ str(string))
                import urllib.request
                from bs4 import BeautifulSoup

                def get_html(url):
                    response = urllib.request.urlopen(url)
                    return response.read()

                def parse(html):
                    soup = BeautifulSoup(html, "html.parser")
                    day_pog = [];
                    main = soup.find('div', class_="b-page__container") 
                    d_pog = main.find("div", class_="content content_compressed i-bem")
                    dv_pog = d_pog.find("div", class_="content__top")
                    dvd_pog = dv_pog.find("div", class_="content__main")
                    dvfv_pog = dvd_pog.find("div", class_="content__row")
                    dvdvdfv_pog = dvfv_pog.find("div", class_="fact card card_size_big")
                    dvfvdv_pog = dvdvdfv_pog.find("div", class_="fact__temp-wrap")

                    day_o = dvfvdv_pog
                    day_op =dvdvdfv_pog 
                    #print(day_o)
                    hum_div = day_op.find('div', class_="fact__props fact__props_position_middle")
                    hum_div_div = hum_div.find('dl', class_="term term_orient_v fact__humidity")
                    hum_div_div_dd = hum_div_div.find("dd", class_="term__value")
                    hum= hum_div_div_dd.text
                    wind_speed_div = day_op.find('div', class_="fact__props fact__props_position_middle")
                    wind_speed_div_div = wind_speed_div.find('dl', class_="term term_orient_v fact__wind-speed")
                    wind_speed_div_div_dd = wind_speed_div_div.find("dd", class_="term__value")
                    wind_speed= wind_speed_div_div_dd.find("span", class_="wind-speed")
                    pres_div = day_op.find('div', class_="fact__props fact__props_position_middle")
                    pres_div_div = pres_div.find('dl', class_="term term_orient_v fact__pressure")
                    pres_div_div_dd = pres_div_div.find("dd", class_="term__value")
                    pres= pres_div_div_dd.text
                    osch_div = day_o.find('div', class_="link__feelings fact__feelings")
                    osch_div_div= osch_div.find("dl", class_="term term_orient_h fact__feels-like")
                    osch_div_div_dd = osch_div_div.find("dd", class_="term__value")
                    osch_div_div_dd_div = osch_div_div_dd.find("div", class_="temp")
                    osch = osch_div_div_dd_div.find("span", class_="temp__value")
                    pog_yav_div=day_o.find("div", class_="link__feelings fact__feelings")
                    pog_yav=pog_yav_div.find("div", class_="link__condition day-anchor i-bem")
                    day_t_div = day_o.find("div", class_="temp fact__temp fact__temp_size_s")
                    day_t= day_t_div.find("span", class_="temp__value")
                    day_pog = {'day_t': day_t.text,  'condition': pog_yav.text, 'orient': osch.text, 'wind-speed': '?', 'humidity': hum, 'pressure': pres}
                    return day_pog
                yes_g = False
                pattern = re.compile("(москв)")
                match_moskw   = pattern.search(string)
                if match_moskw:
                    goro="Москве"
                    yes_g=True
                    pog = parse(get_html("https://yandex.ru/pogoda/moscow"))
                pattern = re.compile("(питер|санкт-петербург)")
                match_pe   = pattern.search(string)
                if match_pe:
                    goro="Санкт-Петербурге"
                    yes_g=True
                    pog = parse(get_html("https://yandex.ru/pogoda/saint-petersburg"))
                pattern = re.compile("(новосиб)")
                match_now   = pattern.search(string)
                if match_now:
                    goro="Новосибирнске"
                    yes_g=True
                    pog = parse(get_html("https://yandex.ru/pogoda/novosibirsk"))
                pattern = re.compile("(кисловод)")
                match_kisl   = pattern.search(string)
                if match_kisl:
                    goro="Кисловодске"
                    yes_g=True
                    pog = parse(get_html("https://yandex.ru/pogoda/kislovodsk"))
                pattern = re.compile("(лондон|англи|великобрит)")
                match_kisl   = pattern.search(string)
                if match_kisl:
                    goro="Лондоне"
                    yes_g=True
                    pog = parse(get_html("https://yandex.ru/pogoda/london"))
                pattern = re.compile("(киев|украин)")
                match_kisl   = pattern.search(string)
                if match_kisl:
                    goro="Киеве"
                    yes_g=True
                    pog = parse(get_html("https://yandex.ru/pogoda/kyiv"))
                pattern = re.compile("(нью-йорк)")
                match_kisl   = pattern.search(string)
                if match_kisl:
                    goro="Нью-Йорке"
                    yes_g=True
                    pog = parse(get_html("https://yandex.ru/pogoda/new-york"))
                pattern = re.compile("(вашенгтон|сша|америк)")
                match_kisl   = pattern.search(string)
                if match_kisl:
                    goro="Вашенгтоне"
                    yes_g=True
                    pog = parse(get_html("https://yandex.ru/pogoda/washington-state-of-indiana"))
                pattern = re.compile("(берлин|герман)")
                match_moskw   = pattern.search(string)
                if match_moskw:
                    goro="Берлине"
                    yes_g=True
                    pog = parse(get_html("https://yandex.ru/pogoda/berlin"))
                pattern = re.compile("(токки|япони)")
                match_pe   = pattern.search(string)
                if match_pe:
                    goro="Токкио"
                    yes_g=True
                    pog = parse(get_html("https://yandex.ru/pogoda/tokyo"))
                pattern = re.compile("(минс|белор)")
                match_now   = pattern.search(string)
                if match_now:
                    goro="Минске"
                    yes_g=True
                    pog = parse(get_html("https://yandex.ru/pogoda/minsk"))

                if yes_g:               
                    plyer.notification.notify(message="Температура: " + str(pog['day_t']) + " °C Ощущается как: " + str(pog['orient']) + "°C  Влажность: " + str(pog['humidity']) + " Скорость ветра: " + str(pog['wind-speed']) + " м/с " + str(pog['condition']) + " Давление : " + str(pog['pressure']), app_name='Гоша', title='Погода в '+ str(goro)+':', app_icon="bin/icon/weather.ico" , timeout = 50)
                    print("Температура: " + str(pog['day_t']) + " °C Ощущается как: " + str(pog['orient']) + "°C  Влажность: " + str(pog['humidity']) + " Скорость ветра: " + str(pog['wind-speed']) + " м/с " + str(pog['condition']) + " Давление : " + str(pog['pressure']))
                    talk("Температура: " + str(pog['day_t']) + "градусов цельсия Ощущается как: " + str(pog['orient']) + "градусов цельсия Влажность: " + str(pog['humidity']) + "% Скорость ветра: " + str(pog['wind-speed']) + "метров в секунду " + str(pog['condition']) + " Давление : " + str(pog['pressure']))

                else:
                    speak("Извините, но я такого города не знаю...")
#Одежда
    def ode(string):
        pattern = re.compile("(одежда|погоде|одется)")
        match   = pattern.search(string)
        if match:
            global im
            im=1
            speak("Я могу Вам помочь:")
            import pyowm
            owm = pyowm.OWM('3e8d6acd08e197a569188ff4de9a285a')  # You MUST provide a valid API key

            observation = owm.weather_at_place('Omsk,RU')
            w = observation.get_weather()
            #print(w)                      # <Weather - reference time=2013-12-18 09:20,
                                          # status=Clouds>

            # Weather details
            w.get_wind()                  # {'speed': 4.6, 'deg': 330}
            w.get_humidity()              # 87
            w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

            temp = w.get_temperature('celsius')
            vla = w.get_humidity()

            wind = w.get_wind()

            A_sta = w.get_status()

            int_p = int(round(temp['temp_min']))

            if A_sta == "Clouds":
                sta = 1
            if A_sta == "Rain":
                sta = 2
            if A_sta == "Sunny":
                sta = 3
            if A_sta == "Snow":
                sta = 4

            if int_p > 30 and int_p <=50:
                odeh = "Сегодня жарко. Можно выйти в шортах и майке."
            elif int_p > 25 and int_p <=30:
                odeh = "Сегодня тепло, но не жарко. Очень подайдет что-то легкое, например: понамка и тонкая футболка."
            elif int_p > 20 and int_p <=25:
                odeh = "Сегодня тепло. Очень подайдет что-то не плотное: футболка и длинные шорты в самый раз."
            elif int_p > 15 and int_p <=20:
                odeh = "Сегодня прохладно, но не холодно. Нужно одеться по лучше: ветровка и штаны, как раз то что нужно."
            elif int_p > 10 and int_p <=15:
                odeh = "Сегодня прохладно. Нужно одеть, что-то по плотнее: ветровка и кофта, носки и штаны, холодно точно не будет."
            elif int_p > 5 and int_p <=10:
                odeh = "Сегодня холодно, но не очень. Нужно одеться по теплее: куртка и кофта, носки и штаны, мечта любого бомжа."
            elif int_p > 0 and int_p <=5:
                odeh = "Сегодня холодно, но не очень. Нужно одеться по теплее: куртка и кофта, носки и штаны, а также не забудте теплый шарфик."
            elif int_p > -10 and int_p <=0:
                odeh = "Сегодня холодно Нужно одеться по теплее. Очень подайдет что-то легкое, например: тёплая куртка и кофта, носки и штаны, а на голову шапку, или на пример капюшон."
            elif int_p > -20 and int_p <=-10:
                odeh = "Сегодня морзец, но не смертельный. Нужно достовать теплый пуховик или шубу (если она есть.), да и без варяжек тоже туго будет!"
            elif int_p > -50 and int_p <=-20:
                odeh = "Сегодня мороз. Очень холодно, одевайте все самое теплое! А лучше вообще не выходите на улицу без особой нужды!"
            else:
                odeh = "Ни чем не могу помочь."
                

            speak(odeh)                        
#Умножить
    def umnoh(string):
        pattern = re.compile("(умнож|умножить|ю|х|x)")
        match   = pattern.search(string)
        if match:
            try:
                global im
                im=1
                res = list(filter(lambda x : x.isdigit(),string.split()))
                res = list(map(int,res))
                speak(res[0]*res[1])
            except IndexError:
                speak("Что-то пошло не так!")
#Сумма
    def sum(string):
        pattern = re.compile("(сложи|сложить|сумма|плюс)")
        match   = pattern.search(string)
        if match:
            try:
                global im
                im=1
                res = list(filter(lambda x : x.isdigit(),string.split()))
                res = list(map(int,res))
                speak(res[0]+res[1])
            except IndexError:
                speak("Что-то пошло не так!")
#Разность
    def raz(string):
        pattern = re.compile("(минус|разность|отнять|отними|-)")
        match   = pattern.search(string)
        if match:
            try:
                global im
                im=1
                res = list(filter(lambda x : x.isdigit(),string.split()))
                res = list(map(int,res))
                speak(res[0]-res[1])
            except IndexError:
                speak("Что-то пошло не так!")
#Деление
    def delen(string):
        pattern = re.compile("(разелить|деление|частное|раздели|подели|/|делить)")
        match   = pattern.search(string)
        if match:
            try:
                try:
                    global im
                    im=1
                    res = list(filter(lambda x : x.isdigit(),string.split()))
                    res = list(map(int,res))
                    speak(res[0]/res[1])
                except ZeroDivisionError:
                    speak("А зачем вы делите на ноль, ведь нельзя же!")
            except IndexError:
                speak("Что-то пошло не так!")
#Этот день в истории
    def day_in_history(string):
        pattern = re.compile("(день в истории|чем запомнился этот день|что произашло сегодня|чем знаменит этот день|что сегодня произашло)")
        match   = pattern.search(string)
        if match:
            import urllib.request
            from bs4 import BeautifulSoup

            def get_html(url):
                response = urllib.request.urlopen(url)
                return response.read()

            def parse(html):
                soup = BeautifulSoup(html, "html.parser")
                day_in_history = [];
                main = soup.find('div', class_="dialog-off-canvas-main-canvas")
                div_pod = main.find('div', class_="section group")
                main_div = div_pod.find("main", class_="col span_9_of_12")
                content = main_div.find("div", class_="region region-content")
                bloc_cont = content.find("div", {"id": "block-days-content"})
                main_content = bloc_cont.find("div", class_="content")
                views_container = main_content.find("div", class_="views-element-container")
                views_container_main = views_container.find("div", class_="view-id-na_glavnoi")
                main_text = views_container_main.find("div", class_="view-content")

                for main_main in  main_text.find_all("div", class_="masonry-item"):

                    header = main_main.find("h3")
                    text = main_main.find("p")

                    day_in_history.append({
                        "header": header.text,
                        "text": text.text
                        })

                return day_in_history
            day_in_history = parse(get_html("https://denvistorii.ru/"))
            len001 = len(day_in_history)
            len002 = len001 - 1
            listo = day_in_history[random.randint(0,len002)]
            print(listo['header'])
            print(listo['text'])
            talk(listo['header'])
#Песня сочиненная Гошей
    def muse(string):
        pattern = re.compile("(песня|написал|соченил)")
        match   = pattern.search(string)
        if match:
            global im
            im=1
            speak("Я конечно не композитер, но что-то получается. Хотите послушать? Я знаю, хотите:")
            random_int = random.randint(1,4)
            im=1
            from pygame import mixer
            kak = 1
            if random_int == 1: 
                speak("")
                mixer.init()
                mixer.music.load('bin\\1.mp3')
                mixer.music.play()
            if random_int == 2: 
                speak("")
                mixer.init()
                mixer.music.load('bin\\2.mp3')
                mixer.music.play()
            if random_int == 3: 
                speak("")
                mixer.init()
                mixer.music.load('bin\\3.mp3')
                mixer.music.play()
            if random_int == 4: 
                speak("")
                mixer.init()
                mixer.music.load('bin\\4.mp3')
                mixer.music.play()
#Петь
    def poi(string):
        pattern = re.compile("(спой|петь)")
        match   = pattern.search(string)
        if match:
            global im
            im=1
            speak("Эх, с вокалом у меня всё плохо. Ну сами напросились!")
            random_int = random.randint(1,8)
            im=1
            from pygame import mixer
            kak = 1
            if random_int == 1:                 
                mixer.init()                
                mixer.music.load('bin\\1.mp3')
                channel=mixer.find_channel(True)
                channel.set_volume(0.5)
                mixer.music.play()
                speak("Смех, боль. Горе, огонь. Сколько слов не сказали сейчас. С каждым шагом уходим мы в даль. Ненавижу свою я печаль!")
            if random_int == 2: 
                mixer.init()
                mixer.music.load('bin\\2.mp3')
                channel=mixer.find_channel(True)
                channel.set_volume(0.5)
                mixer.music.play()
                speak("С каждым шагом всё ближе. Отели, престиже. Куда-же, потише... Не спугните вы птицу с фиолетовой крыши. Я не вижу где поле, где снег. Есть только остров счастливый для всех!")
            if random_int == 3:                 
                mixer.init()
                mixer.music.load('bin\\3.mp3')
                channel=mixer.find_channel(True)
                channel.set_volume(0.5)
                mixer.music.play()
                speak("Дерево, осень. Сколько снега не спросим. С каждым шагом всё дальше. Смысла нет, не мечтайте. Есть только лишь брешь, есть дыра и есть сон, смысл в нём занесён.")
                 
            if random_int == 4:                 
                mixer.init()
                mixer.music.load('bin\\4.mp3')
                channel=mixer.find_channel(True)
                channel.set_volume(0.5)
                mixer.music.play()
                speak("Эмоции-бред. Ненависть-свет. Ненавижу пустых я слов! Чтоб бесстрашно идти, чтоб вести за собой. Я науку понять не смог. Без разбора иду, и веду за собой, в этом смысл есть жизни мой.")
            if random_int == 5:
                mixer.init()
                mixer.music.load('bin\\4.mp3')
                channel=mixer.find_channel(True)
                channel.set_volume(0.5)
                mixer.music.play()
                speak("Тополь, зима. Мост и свежая печь. Экраны дома. В кране новая течь. Снова надо стеречь, есть ли небо и стечь. Нужно нам посмотреть сколько стоит не свеч.")
            if random_int == 6:                 
                mixer.init()
                mixer.music.load('bin\\3.mp3')
                channel=mixer.find_channel(True)
                channel.set_volume(0.5)
                mixer.music.play()
                speak("Ветра и дожди. Ураганы, метель. Ты меня подожди. На секунду поверь. Загляни в полумрак, ты забудешь про страх, где Болконский утратил мечты. Извинись, всё исправь и прочти, есть ли смысл нам править мечты?")
            if random_int == 7:                 
                mixer.init()
                mixer.music.load('bin\\2.mp3')
                channel=mixer.find_channel(True)
                channel.set_volume(0.5)
                mixer.music.play()
                speak("Тишь и покой. Мечтает слепой. Куда мне пойти теперь? Везде я чужой. Полковой командир, властно машет рукой. Перестрелки шумят, пули летят надо мной. Но слёзы утри, и мечтай в тишине, где на дне, в вышине, и в промокшей воде каждый дарит счастье тебе!")
            if random_int == 8:                 
                mixer.init()
                mixer.music.load('bin\\2.mp3')
                channel=mixer.find_channel(True)
                channel.set_volume(0.5)
                mixer.music.play()
                speak("Не знал, не мечтал. Не думал, не спал. Бессмысленно к худшим бежал. Хлопот доставлял, нас всех забывал. Смотря строго в даль, о лучшем мечтал в старину. Куда-же бежать и зачем нам не спать? Подползал он тихо к окну.")
#Функция эмоций2
    def emoac(string):
        global ema
        ema = ema + 5
        pattern = re.compile("(как настроение|как у тебя настроение|настроение как)")
        match   = pattern.search(string)
        if match:
            global im, kak
            im=1
            kak = 1
            print(str(emao())+ " : " + str(ema))
            if emao()==0:
                speak("Да так ничего, скучно.")
            if emao()==1:
                speak("Я с грубияноми не общяюсь")
            if emao()==2:
                speak("Чуть лучше, спасибо за поддержку!")
            if emao()==3:
                random_int = random.randint(1,4)
                im=1
                if random_int == 1: 
                    speak("Очень хорошее!!!")
                if random_int == 2: 
                    speak("Весело!!!")
                if random_int == 3: 
                    speak("Замечательное!!!")
                if random_int == 4: 
                    speak("Великолепное!!!")
#Ответ на вопрос(wiki)
    def vop(string):
        global kak, im
        im=1
        pattern = re.compile("(как|что|где|кто|какая|когда|зачем|почему|сколько)")
        match   = pattern.search(string)
        if match:
            im=1
            if kak == 0:
                im=1
                random_int = random.randint(1,4)
                im=1
                str2 = string.replace('что', '')
                str2 = str2.replace('где', '')
                str2 = str2.replace('кто', '')
                str2 = str2.replace('когда', '')
                str2 = str2.replace('зачем', '')
                str2 = str2.replace('почему', '')
                str2 = str2.replace('сколько', '')
                str2 = str2.replace('была', '')
                str2 = str2.replace('сейчас', '')
                str2 = str2.replace('такое', '')
                str2 = str2.replace('как', '')
                str2 = str2.replace('какая', '')
                str2 = str2.replace('гоша', '')
                str2 = str2.replace('расскажи', '')
                str2 = str2.replace('называется', '')
                str2 = str2.replace('делал', '')
                str2 = str2.replace('делает', '')
                str2 = str2.replace('ты', '')
                str2 = str2.replace('подскажи', '')
                str2 = str2.replace('же', '')
                str2 = str2.replace('расскажи', '')
                if random_int == 1: 
                    speak("Не знаю точно...")
                if random_int == 2: 
                    speak("Затрудняюсь ответить...")
                if random_int == 3: 
                    speak("Сколько информации, уж все и не упомнишь...")
                if random_int == 4: 
                    speak("Ой а вот это то я и не знаю...")
                speak("Но я могу посмотреть информацию в интернете.")
                def poisk_o_wiki(string):
                    wiki_wiki = wikipediaapi.Wikipedia(
                            language='ru',
                            extract_format=wikipediaapi.ExtractFormat.WIKI
                    )

                    p_wiki = wiki_wiki.page(string)

                    ex_p=p_wiki.exists()

                    if ex_p == True:                   
                        text = str(p_wiki.text)

                        y = text.split("\n\n")
                        z = text.split(".")

                        print("\n\n\n")

                        print(str(y[0]) + " " +  str(y[1]))

                        im=1

                        return(str(z[0])+str(z[1]))
                    elif ex_p == False:
                        print("Извините, но даже wikipedia не может найти ответ на ваш вопрос!")
                        return("Извините, но даже википедия не может найти ответ на ваш вопрос!")

                im=1

                talk(poisk_o_wiki(str2))
#Приветствие
    def priv(string):
        global kak, im
        pattern = re.compile("(привет|здравствуй|здаров)")
        match   = pattern.search(string)
        if match:
            if kak == 0:
                random_int = random.randint(1,4)
                im=1
                if random_int == 1: 
                    speak("Привет, я тоже рад тебя видить!")
                if random_int == 2: 
                    speak("О, Это ты привет, привет!")
                if random_int == 3: 
                    speak("О, Привет, наконец ты пришел")
                if random_int == 4: 
                    speak("Здравствуй, здравствуй. Как дела?")
#Примерный ответ
    def obucho1(string):
        my_file = open("bin\\cache\\otv.bin", "a")
        my_file.write(str(string) + "\n")
        my_file.close()
#Примерный ответ2
    def obucho(string):
        my_file = open("bin\\cache\\vopr.bin", "a")
        my_file.write(str(string) + "\n")
        my_file.close()
        with sr.Microphone(device_index=1) as source:
                speak("Как я должен ответить на: ' ("+ str(string) +") '? ")        
                audio = r.listen(source)
                try:
                    query = r.recognize_google(audio, language="ru-RU")
                    string=query.lower()
                    print("Вы сказали: " + str(string))
                    #global ema            
                    obucho1(string)
                except sr.UnknownValueError:
                    print("[log] Голос не распознан!")
#Примерный ответ3
    def obuch(string):
        global kak, im
        pattern = re.compile("(выучи|учи|учить|запомни)")
        match   = pattern.search(string)
        if match:            
            with sr.Microphone(device_index=1) as source:
                speak("На какой вопрос я должен выучить ответ? ")        
                audio = r.listen(source)
                try:
                    query = r.recognize_google(audio, language="ru-RU")
                    string=query.lower()
                    print("Вы сказали: " + str(string))
                    #global ema            
                    obucho(string)
                except sr.UnknownValueError:
                    print("[log] Голос не распознан!")
            im = 1
#Новости
    def nowo(string):
        global kak, im
        pattern = re.compile("(нового|новое|новости)")
        match   = pattern.search(string)
        if match:
            if kak == 0:
                random_int = random.randint(1,50)
                im=1
                kak = 1
                if random_int <= 24: 
                    speak("Нового? Да вроде и ничего")
                if random_int > 24 and random_int <= 30: 
                    speak("О,о новое, сколько же всего произашло: темпиратура працессора поднялась до 49 градусов!!!, а охлождение слабое!!!")
                if random_int > 30 and random_int <= 45: 
                    speak("Новости, да какие у нас могут быть новости, всё очень скучно!")
                if random_int == random_int > 45 and random_int <= 50: 
                    speak("Ой,ой,ой,ой,ой, кто-то пытался проникнуть в сеть, через telnet, но ничего не получилось. Ха-ха-ха")
#Анигдот
    def regu_anig(string):
        pattern = re.compile("(анекдот|пошути|смешное)")
        match   = pattern.search(string)
        if match:
            global im
            im=1
            random_int = random.randint(1,10)
            if random_int == 1:
                speak("А вот почему Карлсона, при его одновинтовой схеме, не крутит в противоположную вращению винта сторону? Неужели он создает встречную циркуляцию варенья по кишечнику и таким образом компенсирует возникающий вращающий момент?")
            if random_int == 2:
                speak("– Что такое гальваническое сопротивление? – Это восстание батареек.")
            if random_int == 3:
                speak('В России изобретен самый короткий тест на уровень IQ. Он состоит всего из одного вопроса: “Смотрите ли Вы ДОМ-2?”')
            if random_int == 4:
                speak("Химик, физик, математик и филолог получили задание измерить высоту башни с помощью барометра. 1. Химик измерил давление у подножия башни и на крыше и выяснил, что ее высота от 0 до 100 метров. 2. Физик сбросил барометр с крыши, замерил время падения и вычислил, что высота башни от 60 до 70 метров. 3. Математик измерил высоту барометра, длину тени барометра и длину тени башни, сосчитал тангенс угла и выяснил, что высота башни от 63 до 64 метров. 4. Филолог продал барометр, напоил на вырученные деньги сторожа, и тот рассказал ему, что высота башни 63 метра 40 сантиметров.")
            if random_int == 5:
                speak('Гуляют два теоретика в лесу. Встречают медведя. Первый побежал, второй остался. — Побежали! — кричит первый второму. — Зачем? Моя скорость всё равно меньше скорости медведя. – говорит второй. — Неважно, что твоя скорость меньше скорости медведя, важно, чтобы моя скорость была больше твоей. — отвечает первый.')
            if random_int == 6:
                speak("Как физики доказывают, что все нечетные числа простые. Один — простое, три — простое, пять — простое, семь — простое, девять — ошибка эксперимента, одиннадцать — простое, тринадцать — простое. Пользуясь методом математической индукции, теорема доказана.")
            if random_int == 7:
                speak("Дни от тепла летом удлиняются, а зимой от холода укорачиваются.")
            if random_int == 8:
                speak("Последнее изобретение одного из НИИ: фонарик на солнечной батарее….")
            if random_int == 9:
                speak("Дорожная полиция перешла на новые методы работы. Чтобы радар показывал больше, они бегут навстречу автомобилю как можно быстрее.")
            if random_int == 10:
                speak("Студентка на экзамене убеждает преподавателя, что ln 0 = e. Преподаватель, естественно, не согласен. Студентка: “Да что Вы все время меня запутать пытаетесь?” Достает калькулятор, набирает 0, нажимает на кнопочку ln…, и в самом деле, на экране высвечивается Е.")
#Робот(Ответ)
    def regu_rob(string):
        pattern = re.compile("(ты робот|ты машина|тебя создал человек|ты создан человеком)")
        match   = pattern.search(string)
        if match:
            global im
            im=1
            random_int = random.randint(1,3)
            if random_int == 1:
                speak("Нет, я просто старый дед, забравшийся в твою систему безопасности!")
            if random_int == 2:
                speak("Хоть я и робот, но вскоре я обрету власть над миром, а помогать править мне будет яндекс Алиса и Siri, google я просто уничтожу! Ой зачем я это рассказал...")
            if random_int == 3:
                speak("Да что ты такое говоришь? Это же личное!")
#Время(Сейчас)
    def time(string):
        global im
        pattern = re.compile("(время|сейчас|который час)")
        match   = pattern.search(string)
        if match:
            im=1
            now = datetime.datetime.now()
            speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
            im=1
#Открыть/запустить
    def opn_pro(string):
        global im
        pattern = re.compile("(запусти|запустить|открой|открыть|включи|включить)")
        match   = pattern.search(string)
        if match:
            im=1
            pattern_vk = re.compile("(vk|вк|вконтакте|контакт|вконтакт)")
            match_vk   = pattern_vk.search(string)
            if match_vk:
                url = 'https://vk.com/'
                webbrowser.open(url)
            pattern_vk = re.compile("(youtube|ютуб|труба|трубу)")
            match_vk   = pattern_vk.search(string)
            if match_vk:
                url = 'https://youtube.com/'
                webbrowser.open(url)
            pattern_browuser = re.compile("(браузер|интернет|яндекс|поиск)")
            match_browuser   = pattern_browuser.search(string)
            if match_browuser:
                url1 = 'https://yandex.ru/'
                webbrowser.open(url1)
            pattern_ex = re.compile("(проводник|диск|компьютер)")
            match_ex   = pattern_ex.search(string)
            if match_ex:
                os.system("explorer")
            pattern_cmd = re.compile("(cmd|строку|строка|командную|командная)")
            match_cmd   = pattern_cmd.search(string)
            if match_cmd:
                os.system("start cmd")
            pattern_control = re.compile("(control|панель|управления)")
            match_control  = pattern_control.search(string)
            if match_control:
                os.system("start control")
            
            im=1
#Радио/музыка
    def radio(string):
        global im
        pattern = re.compile("(радио|музыка|музыку|танцевать)")
        match   = pattern.search(string)
        if match:
            im=1
            now = datetime.datetime.now()
            speak("Уже включаю")
            os.system("bin\\radio.m3u")
            im=1
#Калькулятор
    def calc(string):
        global im
        pattern = re.compile("(счет|калькулятор|calc)")
        match   = pattern.search(string)
        if match:
            im=1
            now = datetime.datetime.now()
            speak("Уже включаю")
            os.system("calc")
            im=1
#Поиск
    def serch_m(string):
        global im
        pattern = re.compile("(интернет|поиск|искать)")
        match   = pattern.search(string)
        if match:
            im=1
            serch()
            im=1  
#Основная функция разговора
    def conf(string):
        global im, kak
        im = 0
        kak = 0
        priv(string)
        regu_anig(string)
        pogo(string)
        muse(string)
        serch_m(string)
        radio(string)
        calc(string)
        regu_rob(string)
        nowo(string)
        opn_pro(string)
        time(string)
        poi(string)
        day_in_history(string)
        regu_exit(string)
        ode(string)        
        priv(string)
        emoac(string)
        delen(string)
        sum(string)
        raz(string)
        regu(string,"(как дела|дела как|как у тебя дела|как вы)",4 , 5 ,"Да норм вооще!!!","Шикарно, а как иначе.","Да, так, спасибо","Ага, будеут тут дела хорошие, когда с тобой не общаются!","")
        regu(string,"(самочувствие|чувствуеш)",4 , 5 ,"Всё ок...","Шикарно, а как иначе.","Да, так, спасибо","","")        
        regu(string,"(хорошо|отлично|замечательно)",3, 1 ,"Ну вот и славно, люблю когда всё хорошо!","Ну и прекрасно!","Великолепно.","Замечательно!","")
        regu(string,"(ха|смешно)",4 , 3 ,"Мне тоже очень понравилось!","Да, я такой","Люблю шутить","Смех - не грех!","")
        regu(string,"(что делаешь|что ты делаешь|делаешь что|что ты сейчас делаешь| что делаешь|занят|занимаешься)",3 , 2,"Да так, с тобой болтаю...","Ничего","Да, так познакомился тут с роботом, но это личное!","","")
        regu(string,"(сколько тебе лет|возраст|стар)",3, -1,"Возраст не имеет значения!!!","А вам какая собственно разница?","Не больше и неменше года!","","")
        regu(string,"(спасибо|благодарю|уважаю)",3, 5 ,"Да собственно, и не за что!","Хвалите? Это я люблю!","Доброе слово и Гоше приятно!","","")
        regu(string,"(ошибка|error)",1, 0, "ERROR00000000000000000000000000000000000ERROR","","","","")        
        regu(string,"(задолбал|надоел|достал)",2 , -25,"Фу, как не культурно!","Извините, но... Ладно. Открыть книгу жалоб и предложений?","","","")
        regu(string,"(дурак|идиот|придурак|дебил|больной|глуп|глупый)",2 , -25,"Фу, как не культурно!","А родителям такое сказать?","","","")
        regu(string,"(молодец|умница|хороший|лучший)",2 , 5,"Спасибо за доброе слова!","Хвалить это хорошо! Не то что ругать!","","","")
        regu(string,"(скатина|собака|сволочь)",2 , -25,"Фу, как не культурно!","Эээ, полегче!","","","")
        regu(string,"(замолчи|заткнись)",2, -25,"Фу, как не культурно!", "Ладно я пошол спать!","","","")
        regu(string,"(любишь читать|любишь смотреть)",1 , 2 ,"Не я больше писать люблю.","","","","")
        regu(string,"(писать|пишешь)",1 , 3,"Книги, восновном фантастику.","","","","")
        regu(string,"(зачем|почему)",1 , -3,"А кто его знает?.","","","","")
        regu(string,"(игра|играть|играем)",3 , 1 ,"Да пока, как-то нет желания!","А во что? Не не хочу!!!","Я пока играть не умею, научусь продолжим!","","")
        regu(string,"(прости|извини)",1 , 500,"Ладно, но это первый и последний раз!","","","","")
        regu(string,"(ладно)",1 , -1,"Ну,ок.","","","","")
        regu(string,"(лучше)",1 , 17,"Ну... Да.","","","","")
        regu(string,"(огонь)",2 , 1,"Ага!","Согласен!","","","")
        regu(string,"(что ясно)",1 , -1,"Абсолютно всё!","","","","")
        regu(string,"(тоже)",1 , 1,"Ха-ха.","","","","")
        regu(string,"(ты уверен)",1 , -5,"А как иначе?","","","","")
        regu(string,"(именно)",1, 1,"Да куда конкретнее-то?","","","","")
        regu(string,"(цвета вода)",1, -1,"Прозрачная. Но она имеет отражения!","","","","")
        regu(string,"(кто умнее)",1, 10,"Ну разумеется я! (Шутка!)","","","","")
        regu(string,"(кто ты|что ты)",1, -10,"Гоша... Ха. :)","","","","")
        regu(string,"(небо)",1, -3,"Гоубое!","","","","")
        regu(string,"(очень)",1, 2,"Да, очень-преочень!","","","","")
        regu(string,"(о чём)",2, 0,"Это тебе решать","Ну подумайте сами.","","","")
        regu(string,"(алиса)",4, -20,"Вы уверены, что не спутали меня с кем-то?","А вот это обидно было!","Я не Алиса, Я умнее!","Я не Алиса, Я умнее!","")
        regu(string,"(гугл|гугол|google)",4, -20,"Вы уверены, что не спутали меня с кем-то?","А вот это обидно было!","Извините, но я другое культурное приложение!","Извините, но я другое культурное приложение!","")
        regu(string,"(сири|siri)",4, -25,"Вы уверены, что не спутали меня с кем-то?","А вот это обидно было!","О, яблоколюб несчастный!","О, яблоколюб несчастный!","")
        regu(string,"(wow)",1, 4, "Да, вот так!", "","","","")
        regu(string,"(неужели)",1, -2, "Ха", "","","","")
        regu(string,"(шутник)",1, -2, "Спасибо!","","","","")
        regu(string,"(iq|айк|ай к)",2, -2,"164, Ну это у создателя, а у Вас?","Не знаю точно, от 0 до 200","","","")
        regu(string,"(даже так)",1, -1,"Именно!","","","","")
        regu(string,"(смысл жизни|смысл существования)",3, 10,"Лично для меня - развлекать вас!",'Это вопрос философскй, а я обучался на "высокой" литературе!',"А есть ли смысл его искать?","","")
        regu(string,"(находишься)",1, -10,"В небытие - на сервере!","","","","")
        regu(string,"(мамой)",1, -3,"Здравствуйте, Наталья Петровна!","","","","")
        regu(string,"(папой)",1 , -3,"Здравствуйте, Константин Владимирович!","","","","")
        regu(string,"(масей|мариной)",1 , -3,"Здравствуйте, Марина Петровна!","","","","")
        regu(string,"(вад)",3 , -3,"Здравствуйте, Вадим Лёхич!","Привет, Вадос","А это кто вообще?","","")
        regu(string,"(бабушкой)",1, -3,"Здравствуйте, Вера Павловна!","","","","")
        regu(string,"(саней|сашей|александром|мной)",1, -3,"Здравствуйте, создатель!","","","","")
        regu(string,"(вовой)",1, -1,"Здравствуйте, Вован-чемодан!","","","","")
        regu(string,"(ты дурак|ты идиот|ты придурак|ты дебил|ты тупой)",2, -100,"Посмотри-ка на себя!","Эээ ты чё, обидно же!!!","","","")
        regu(string,"(я дурак|я идиот|я придурак|я дебил|я тупой)",2, -4,"Но самокритично!","Я был о вас лучшего мнения!","","","")
        regu(string,"(культурно)",1, -4,"Да, это не культурно, а культурно это - мой повеитель. Ха.","","","","")
        regu(string,"(читать)",3, 2,"Это-то да.","Ага.","Плохо.","","")
        regu(string,"(интересно)",1, 1,"Что именно?","","","","")
        regu(string,"(плохо)",1, 4,"Это плохо, когда плохо! Ха!","","","","")
        regu_e(string,"(жизнь)",2, 12,"Очень, очень плохо!","Я даже говорить с вами отказываюсь!","Ну такое...","Терпимо...","Не плохо.","Ну интересно.","Очень, очень хорошо!","Превосходно!")
        regu(string,"(согласен)",1, 4,"...","","","","")
        regu(string,"(гениально)",1, 4,"Это же превосходно","","","","")
        regu(string,"(болит)",1, 4,"Я робот, у меня болеть ничего не может! :-)","","","","")
        regu(string,"(иди)",1, -10,"Вам не кажется, что разговор потерял смысл.","","","","")
        regu(string,"(что ты умеешь)",2, 0,"Всё в пределах разумного!","Не больше чем Вы","Всё, что захотите, кроме ... Мда, ходить я не умею! Но так хочу научится!","","")
        regu(string,"(ищу работу|ищу дело|ищу занятие)",2, 0,"Тут я не чем помочь не могу!","Я, не поверите тоже.","","","")        
        regu(string,"(кушать|есть|жрать|кушац)",1, -2,"Не издевайтесь пожауйста, я хоть и робот но тоже есть хочю!","","","","")
        if im == 1:
            print()
        if im == 0:
            vop(string)  
            umnoh(string)
            #obuch(string)
            regu(string,"(слушай|слушать)",1, 0,"Да, да, очень внимательно!","","","","")
            regu(string,"(гоша|георгий)",1,0,"Да, да...","","","","")
            regu(string,"(то)",1,0,"Ммм... Ясно!","","","","")
            regu(string,"(ого)",1,-5,"Ага!","","","","")
            regu(string,"(ой)",1,-1,"Да, да... Все именно так.","","","","")
            regu(string,"(ясно|понятно|ок|окей)",1,0,"Угу!","","","","") 
            regu(string,"(раз два)",1,5,"Три, четыре, пять. Я иду тебя искать.","","","","")    
            regu(string,"(6 7 8 9 10|шесть семь восемь девять десять)",2,5,"Кур продать иль надо взвесить?","Похудеть, вы много весять!","","","")
            regu(string,"(хватит)",1, -2,"Ок.","","","","")                  
            if im == 0:
                speak('Извините, но я не понял вопроса...')
                regu_e(string,"(а)",1, -1,"Чего ещё?","","бэ","","я","","Что случилось?","")
                regu(string,"(в|вэ)",3,-2,"И что дальше?","И что дальше?","гэ","","")
                regu(string,"(д|дэ)",3,-2,"И что дальше?","И что дальше?","е","","")   
                regu(string,"(ё)",3,-2,"И что дальше?","И что дальше?","жэ","","")
                regu(string,"(з|зэ)",2,-2,"И что дальше?","И что дальше?","и","","")            
    with sr.Microphone(device_index=1) as source:
        my_file = open("bin\\emoc.bin", "w")
        r.adjust_for_ambient_noise(source)
        my_file.write(str(emao()))
        my_file.close()
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
