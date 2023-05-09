import random
from playsound import playsound
import time
import os
from os.path import exists
import speech_recognition as sr
import wave

def load_transcription():
    transcription = []
    with open("marathi_number_transcription.txt") as file:
        for line in file:
            transcription.append(line.split())
    return transcription

def cleanup():
    for file in (["answer.wav"]):
        if exists(file):
            os.remove(file)
    
transcription = load_transcription()

while True:
    number = random.randint(1,10)
    times = random.randint(1,10)
    playsound("numbers/" + str(number) + ".wav")
    playsound("times/" + str(times) + ".wav")
    time.sleep(1)

    # listen to the answer
    while True:
        answer = ""
        print("Please state your answer in marathi")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            with open("answer.wav", "wb") as f:
                f.write(audio.get_wav_data())

            print("Recognizing the marathi number Now .... ")
        
            try:
                answer = r.recognize_google(audio, language="mr-IN")
                print("You have said: " + answer)
                break
            except Exception as e:
                print("Error :  " + str(e))
                playsound("prompt/repeat.wav")
                continue

    # check answer
    product = number * times

    number_transcriptions = []

    if len(transcription) >= product:
        number_transcriptions = transcription[product - 1]

    is_correct = False

    for s in number_transcriptions:
        if s == answer:
            is_correct = True

    if is_correct:
        playsound("prompt/correct.wav")
    else:
        print(answer)
        playsound("prompt/incorrect.wav")

    playsound("numbers/" + str(number) + ".wav")
    playsound("times/" + str(times) + ".wav")
    product = number * times
    fname = "numbers/" + str(product) + ".wav"
    if exists(fname):
        playsound(fname)
    cleanup()
    time.sleep(1)