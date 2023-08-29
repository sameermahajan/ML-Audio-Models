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

class_to_number = {0 : 1,  1 : 10,  2 : 100,  3 : 11,  4 : 12,  5 : 13,  6 : 14,  7 : 15,  8 : 16,  9 : 17,  10 : 18,  11 : 19,  
                   12 : 2,  13 : 20,  14 : 21,  15 : 22,  16 : 23,  17 : 24,  18 : 25,  19 : 26,  20 : 27,  21 : 28,  22 : 29,  
                   23 : 3,  24 : 30,  25 : 31,  26 : 32,  27 : 33,  28 : 34,  29 : 35,  30 : 36,  31 : 37,  32 : 38,  33 : 39,  
                   34 : 4,  35 : 40,  36 : 41,  37 : 42,  38 : 43,  39 : 44,  40 : 45,  41 : 46,  42 : 47,  43 : 48,  44 : 49,  
                   45 : 5,  46 : 50,  47 : 51,  48 : 52,  49 : 53,  50 : 54,  51 : 55,  52 : 56,  53 : 57,  54 : 58,  55 : 59,  
                   56 : 6,  57 : 60,  58 : 61,  59 : 62,  60 : 63,  61 : 64,  62 : 65,  63 : 66,  64 : 67,  65 : 68,  66 : 69,  
                   67 : 7,  68 : 70,  69 : 71,  70 : 72,  71 : 73,  72 : 74,  73 : 75,  74 : 76,  75 : 77,  76 : 78,  77 : 79,  
                   78 : 8,  79 : 80,  80 : 81,  81 : 82,  82 : 83,  83 : 84,  84 : 85,  85 : 86,  86 : 87,  87 : 88,  88 : 89,  
                   89 : 9,  90 : 90,  91 : 91,  92 : 92,  93 : 93,  94 : 94,  95 : 95,  96 : 96,  97 : 97,  98 : 98,  99 : 99}


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
