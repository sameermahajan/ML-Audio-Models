import speech_recognition as sr
from playsound import playsound

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Please say something: \n")
    audio = r.listen(source)
    fname = input("Please enter file name to save recording to: \n")
    with open(fname+".wav", "wb") as f:
        f.write(audio.get_wav_data())
    print("Recorded successfully\n")
        
