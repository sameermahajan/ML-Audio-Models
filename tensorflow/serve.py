import tensorflow as tf

CONCRETE_INPUT = "waveform"

def get_spectrogram(waveform):
    # Convert the waveform to a spectrogram via a STFT.
    spectrogram = tf.signal.stft(
                      waveform, frame_length=255, frame_step=128)
    # Obtain the magnitude of the STFT.
    spectrogram = tf.abs(spectrogram)
    # Add a `channels` dimension, so that the spectrogram can be used
    # as image-like input data with convolution layers which expect
    # shape (`batch_size`, `height`, `width`, `channels`).
    spectrogram = spectrogram[..., tf.newaxis]
    return spectrogram

def model_exporter(model: tf.keras.Model):
    m_call = tf.function(model.call).get_concrete_function(
           tf.TensorSpec(
                 shape=[None, 124, 129, 1], dtype=tf.float32, name=CONCRETE_INPUT
           )
    )

    @tf.function(input_signature=[tf.TensorSpec([None], tf.string)])
    def serving_fn(string_input):
        decoded_input = tf.io.decode_base64(string_input)
        x, sample_rate = tf.audio.decode_wav(tf.squeeze(decoded_input), desired_channels=1, desired_samples=16000,)
        x = tf.squeeze(x, axis=-1)
        waveform = x
        x = get_spectrogram(x)
        x = x[tf.newaxis,...]
        prediction = model(x)
        #return {"number": class_to_number[np.argmax(prediction.eval(session=tf.compat.v1.Session()))]}
        #tf.compat.v1.disable_eager_execution()
        #pred = tf.argmax(prediction).eval(session=tf.compat.v1.Session())
        #return {"number": class_to_number[pred]}
        return prediction

    return serving_fn

model = tf.keras.models.load_model("marathi-100")
tf.saved_model.save(
    model,
    "/mnt/c/ML/Tables/ML-Audio-Models/tensorflow/serve/1",
    signatures={"serving_default": model_exporter(model)},
)
