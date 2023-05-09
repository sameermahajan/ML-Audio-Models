import random
from playsound import playsound
from os.path import exists

while True:
    number = random.randint(1,10)
    times = random.randint(1,10)
    playsound("no_silence_numbers/" + str(number) + ".wav")
    playsound("no_silence_times/" + str(times) + ".wav")

    # listen to the answer
    answer = input("Enter your answer: ")

    # check answer
    product = number * times

    if answer == str(product):
        playsound("prompt/correct.wav")
    else:
        playsound("prompt/incorrect.wav")
        print(answer)
        fname = "numbers/" + answer + ".wav"
        if exists(fname):
            playsound(fname)
        playsound("prompt/incorrect.wav")

    playsound("numbers/" + str(number) + ".wav")
    playsound("times/" + str(times) + ".wav")
    product = number * times
    fname = "numbers/" + str(product) + ".wav"
    if exists(fname):
        playsound(fname)