import wave
import sys

wf = wave.open(sys.argv[1], 'rb')
print (input, "#channels = ", wf.getnchannels(), "#frames = ", wf.getnframes(), "sample width = ", wf.getsampwidth(), "sample rate = ", wf.getframerate())