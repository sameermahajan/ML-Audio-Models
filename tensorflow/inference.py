import tensorflow as tf
from keras import models

model = tf.keras.models.load_model("marathi-20")
model.summary()

x = tf.io.read_file('../samples/1/1_0.wav')
x, sample_rate = tf.audio.decode_wav(x, desired_channels=1, desired_samples=16000,)
x = tf.squeeze(x, axis=-1)
waveform = x
x = get_spectrogram(x)
x = x[tf.newaxis,...]
prediction = model(x)
