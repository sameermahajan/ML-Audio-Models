import tensorflow as tf
from keras import models
import numpy as np
import sys

def get_spectrogram(waveform):
  # Convert the waveform to a spectrogram via a STFT.
  spectrogram = tf.signal.stft(
      waveform, frame_length=255, frame_step=128)
  # Obtain the magnitude of the STFT.
  spectrogram = tf.abs(spectrogram)
  # Add a `channels` dimension, so that the spectrogram can be used
  # as image-like input data with convolution layers (which expect
  # shape (`batch_size`, `height`, `width`, `channels`).
  spectrogram = spectrogram[..., tf.newaxis]
  return spectrogram

def main(file_name):
    model = tf.keras.models.load_model("../ML-Audio-Models/tensorflow/marathi-40")
    #model.summary()

    x = tf.io.read_file(file_name)
    x, sample_rate = tf.audio.decode_wav(x, desired_channels=1, desired_samples=16000,)
    x = tf.squeeze(x, axis=-1)
    waveform = x
    x = get_spectrogram(x)
    x = x[tf.newaxis,...]
    prediction = model(x)
    #print (prediction)
    print (file_name, np.argmax(prediction))

if __name__ == '__main__':
    main(sys.argv[1])