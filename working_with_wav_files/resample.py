from pydub import AudioSegment as am
import sys

sound = am.from_file(sys.argv[1], format='wav', frame_rate=44100)
sound = sound.set_frame_rate(48000)
sound.export(sys.argv[2], format='wav')