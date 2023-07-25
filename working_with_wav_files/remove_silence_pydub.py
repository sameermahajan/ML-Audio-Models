from pydub import AudioSegment, silence 
import sys
import os 
from math import ceil


def remove_silence(file_name, output_file_name):
    fn =  file_name.split('/')[-1].split(".wav")[0]
    audio = AudioSegment.from_file(file_name, format="wav")

    min_silence_duration = 200
    silence_threshold = -54

    chunks = silence.split_on_silence(
        audio,
        min_silence_len=min_silence_duration,
        silence_thresh=silence_threshold
    )

    output = AudioSegment.empty()
    for chunk in chunks:
        output += chunk
        
    output.export(output_file_name, format="wav")
    

if __name__ == "__main__":
    remove_silence(sys.argv[1], sys.argv[2])
