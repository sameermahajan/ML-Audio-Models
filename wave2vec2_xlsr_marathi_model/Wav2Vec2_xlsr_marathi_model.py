from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from datasets import load_dataset
import torch
import os
import csv
 
# load model and tokenizer
#  processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
#  model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
processor = Wav2Vec2Processor.from_pretrained("sumedh/wav2vec2-large-xlsr-marathi")
model = Wav2Vec2ForCTC.from_pretrained("sumedh/wav2vec2-large-xlsr-marathi")
     
# load dummy dataset and read soundfiles
#  ds = load_dataset("common_voice", "en", split="validation")
 
audio_array, _ = librosa.load("10_10.wav", sr=sr)

input_values = processor(audio_array, return_tensors="pt", padding=True).input_values
# tokenize
#  input_values = processor(ds[0]["audio"]["array"], return_tensors="pt", padding="longest").input_values  # Batch size 1
 
# retrieve logits
logits = model(input_values).logits
 
# take argmax and decode
predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(predicted_ids)


def predict(audio_file):
    audio_array, _ = librosa.load(audio_file, sr=sr)

    input_values = processor(audio_array, return_tensors="pt", padding=True).input_values
    # tokenize
    #  input_values = processor(ds[0]["audio"]["array"], return_tensors="pt", padding="longest").input_values  # Batch size 1

    # retrieve logits
    logits = model(input_values).logits

    # take argmax and decode
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)
    return transcription

lang = ''
for root, dirs, files in os.walk("C:/Users/GS-3447/Desktop/kivymlspeechpoc/"):
    for file in files:
        if file.endswith(".wav"):
            print(root.replace("\\","/")+'/'+file)
            with open("C:/Users/GS-3447/Desktop/myfile_phoneme_sumedh.csv", 'a', encoding="utf-8") as file1:
                writer = csv.writer(file1)
#                 machine = sr.AudioFile(root.replace("\\","/")+'/'+file)
                audio = root.replace("\\","/")+'/'+file
#                 with machine as source:
#                     audio = r.record(source)
                if 'english' in root:
                    lang = 'en'
                elif 'marathi' in root:
                    lang = 'marathi'
                else:
                    lang = 'en'
                writer.writerow([root.replace("\\","/")+'/'+file,predict(audio)])