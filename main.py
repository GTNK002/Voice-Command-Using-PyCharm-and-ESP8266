''' Please check out my Youtube video for step by step process
https://www.youtube.com/watch?v=qdn1H1xotFs&ab_channel=RoboscienceGtnk
librery required pip install pyserial, SpeechRecognition, pyttsx3, PyAudio '''

import serial
import speech_recognition as sr
import time
import pyttsx3


serialcommunication = serial.Serial('COM3', 9600)  # use your com port

serialcommunication.timeout = 1


running = True


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    print('Listening.......')
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
            speak("I am waiting")
    return said.lower()


def run():
    text = get_audio()

    if 'turn on' in text:
        speak('turning on the ESP')
        serialcommunication.write('on'.encode())
        time.sleep(0.5)
        print(serialcommunication.readline().decode('utf-8'))
    elif 'turn off' in text:
        speak('turning off the ESP')
        serialcommunication.write('off'.encode())
        time.sleep(0.5)
        print(serialcommunication.readline().decode('utf-8'))
    elif 'shutdown' in text:
        speak('shutting off the ESP')
        print('shutting off the ESP')
        serialcommunication.close()
        global running
        running = False
    else:
        speak('Invalid command')
        print('Invalid command')


while running:
    run()
