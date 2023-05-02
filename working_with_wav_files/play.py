# Import packages
from pydub import AudioSegment
from pydub.playback import play  
# Play
playaudio = AudioSegment.from_file("1.wav", format="WAV>")
play(playaudio)

