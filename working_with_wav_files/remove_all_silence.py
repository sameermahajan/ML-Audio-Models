import remove_silence

for i in range(1,2):
    input = "..\\app\\numbers\\" + str(i) + ".wav"
    output = str(i) + ".wav"
    print ()
    remove_silence.main(["0", input, output])