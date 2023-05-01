import wave

for i in range(1,100):
    input = "..\\app\\numbers\\" + str(i) + ".wav"
    wf = wave.open(input, 'rb')
    print (input, "#channels = ", wf.getnchannels(), "#frames = ", wf.getnframes(), "sample width = ", wf.getsampwidth(), "sample rate = ", wf.getframerate())