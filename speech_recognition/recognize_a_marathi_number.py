import speech_recognition as sr
import wave
import os
currentNum = int(input("Enter Number : "))
prompt = ""
count = 0
while prompt != "exit":
    if not os.path.exists("./live_samples/"+str(currentNum)):
        os.mkdir("./live_samples/"+str(currentNum))
    count = len(os.listdir("./live_samples/"+str(currentNum)))
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say the number "+str(currentNum)+" in marathi")

        audio = r.listen(source)
        with open("number.wav", "wb") as f:
            f.write(audio.get_wav_data())
        with open("./live_samples/"+str(currentNum)+"/"+str(currentNum)+"_"+str(count)+".wav", "wb") as f:
            f.write(audio.get_wav_data())
    count = count + 1
    # prefix the audio recording with 'akda' for better recognition
    infiles = ["akda.wav", "number.wav"]
    outfile = "check.wav"

    data= []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()

    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    output.writeframes(data[0][1])
    output.writeframes(data[1][1])
    output.close()

    # read the saved .wav file with the 'akda' prefix
    check = sr.AudioFile('check.wav')
    with check as source:
        audio = r.record(source)

    print("Recognizing the marathi number Now .... ")

    try:
        print("You have said \n" + r.recognize_google(audio))
        print("Audio Recorded Successfully \n ")
    except Exception as e:
        print("Error :  " + str(e))
    # write audio
    with open("recorded.wav", "wb") as f:
        f.write(audio.get_wav_data())
    
    prompt = input("To continue recording, type 'c' \nTo change number type 'change' \nTo exit type 'exit' \nEnter your choice : ")
    if prompt == "change":
        currentNum = int(input("Enter Number : "))
        count = 0
