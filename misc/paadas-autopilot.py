import random
from playsound import playsound
import time
from os.path import exists

while True:
    number = random.randint(1,10)
    times = random.randint(1,10)
    playsound("numbers/" + str(number) + ".wav")
    playsound("times/" + str(times) + ".wav")
    time.sleep(1)
    playsound("prompt/correct.wav")
    playsound("numbers/" + str(number) + ".wav")
    playsound("times/" + str(times) + ".wav")
    product = number * times
    fname = "numbers/" + str(product) + ".wav"
    if exists(fname):
        playsound(fname)
    time.sleep(1)