import time
import requests
import datetime
import subprocess
from gtts import gTTS
import playsound  #use 1.22
import os
import speech_recognition as sr
import wikipedia
import webbrowser
from selenium import webdriver
import wolframalpha

def respond(output):
    cnt=0
    print(output)
    cnt+=1
    response = gTTS(text = output, lang = 'en')
    file = str(cnt) + ".mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)

def talk():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        input.adjust_for_ambient_noise(source, duration = 1)
        audio = input.listen(source)
        data = ""
        try:
            data = input.recognize_google(audio)
            print("Your question is, " + data)
        except sr.UnknownValueError:
            print("Sorry, please repeat again..")
        return data



if __name__ == '__main__':
    respond("Hello, I'm Ash, your personal desktop assistant")

    while(1):
        respond("How can I help you?")
        text = talk().lower()

        if text == 0:
            continue

        if 'stop' in str(text) or 'exit' in str(text) or 'bye' in str(text):
            respond("See ya")
            break

        if 'wikipedia' in text:
            respond('Searching Wikipedia')
            text = text.replace('wikipedia', '')
            results = wikipedia.summary(text, sentences = 3)
            respond('According to wikipedia..')
            respond(results)

        elif 'time' in text:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            respond('The time is '+strTime)
            #respond(strTime)

        elif 'gmail' in text:
            webbrowser.open_new_tab('https://www.gmail.com')
            respond('Gmail is now opened..')
            time.sleep(5)

        elif 'who are you' in text or 'what can you do' in text:
            respond('I am Ash, your personal desktop assistant. I can fetch information for you, perform mathematical calculations, take photo, open applications, get weather details.')

        elif 'calculate' in text:
            question = talk()
            app_id = 'API key' #Login to wolframealpha and put API key here
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            respond('The answer is '+answer)

        elif "who made you" in text or "who created you" in text or "who discovered you" in text:
            respond("I was built by Harsha")

        elif 'search' in text:
            text = text.replace('search', '')
            webbrowser.open_new_tab(text)
            time.sleep(5)

        elif 'open google' in text:
            webbrowser.open_new_tab('https://www.google.com')
            respond('Google is now opened..')
            time.sleep(5)

        elif 'open youtube' in text:
            webbrowser.open_new_tab('https://www.youtube.com')
            respond('Youtube is now opened..')
            time.sleep(5)
        
        elif "weather" in text:
            respond("what is the city name")
            city_name=talk()
            api_key="API key"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                respond(" Temperature is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
        
        elif 'shut down' in text:
            respond('System will be shutting down in 10 seconds..')
            subprocess.call(['shut down', '/s', '/t', '10'])

        elif 'restart the system' in text:
            respond('Preparing to restart...')
            subprocess.call(['shut down', '/r'])

        else:
            respond("No keyword detected. Try Again..")
