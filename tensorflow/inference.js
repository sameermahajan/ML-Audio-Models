const tf = require('tensorflow.js');
const fs = require('fs');

async function get_spectrogram(waveform) {
  // Convert the waveform to a spectrogram via a STFT.
  const spectrogram = tf.signal.stft(
    waveform, 255, 128, 'complex64'
  );
  // Obtain the magnitude of the STFT.
  const absSpectrogram = tf.abs(spectrogram);
  // Add a `channels` dimension, so that the spectrogram can be used
  // as image-like input data with convolution layers (which expect
  // shape (`batch_size`, `height`, `width`, `channels`).
  const spectrogramWithChannels = absSpectrogram.expandDims(-1);
  return spectrogramWithChannels;
}

async function loadModelAndPredict() {
  const model = await tf.loadLayersModel('marathi-20/model.json');
  model.summary();

  const audioBuffer = fs.readFileSync('../samples/1/1_0.wav');
  const wavData = await tf.audio.decodeWav(audioBuffer, {
    desiredChannels: 1,
    desiredSamples: 16000,
  });
  const waveform = tf.squeeze(wavData.tensor, -1);
  const spectrogram = await get_spectrogram(waveform);
  const prediction = model.predict(spectrogram.expandDims(0));
  const result = prediction.argMax(1).dataSync()[0];
  console.log(result);
}

loadModelAndPredict();
