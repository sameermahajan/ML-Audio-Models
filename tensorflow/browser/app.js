//import { performASR } from "./performASR.js";

let mediaRecorder = null;
let chunks = [];

const recordButton = document.getElementById("recordButton");
const stopButton = document.getElementById("stopButton");
const playButton = document.getElementById("playButton");

recordButton.addEventListener("click", startRecording);
stopButton.addEventListener("click", stopRecording);
playButton.addEventListener("click", playRecording);

function startRecording() {
  chunks = [];
  navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    recordButton.style.backgroundColor = "red";
    stopButton.disabled = false;
    playButton.disabled = true;
  });

  mediaRecorder.addEventListener("dataavailable", (event) => {
    chunks.push(event.data);
  });
}

function stopRecording() {
  mediaRecorder.stop();
  mediaRecorder.addEventListener("dataavailable", (event) => {
    chunks.push(event.data);
  });

  recordButton.style.backgroundColor = "";
  stopButton.disabled = true;
  playButton.disabled = false;
}

const audio = new Audio();
audio.controls = true;
document.body.appendChild(audio);

function playRecording() {
  const blob = new Blob(chunks, { type: "audio/ogg; codecs=opus" });
  const audioURL = URL.createObjectURL(blob);
  audio.src = audioURL;
  audio.play();
  createSpectrogram(audio);
  performASR(audio)
}

mediaRecorder.addEventListener("stop", (event) => {
  const audioBlob = new Blob(chunks, { type: "audio/ogg; codecs=opus" });
  const audioURL = URL.createObjectURL(audioBlob);
  const audio = new Audio(audioURL);
  audio.controls = true;
  document.body.appendChild(audio);
  audio.play();
  chunks = [];
});

function createSpectrogram(audio) {
  const canvas = document.getElementById("spectrogram");
  const context = canvas.getContext("2d");
  context.clearRect(0, 0, canvas.width, canvas.height);
  const audioContext = new AudioContext();
  const source = audioContext.createMediaElementSource(audio);
  const analyser = audioContext.createAnalyser();
  source.connect(analyser);
  analyser.connect(audioContext.destination);
  analyser.fftSize = 2048;
  const bufferLength = analyser.frequencyBinCount;
  const dataArray = new Uint8Array(bufferLength);
  const width = canvas.width;
  const height = canvas.height;
  const imageData = context.createImageData(width, height);
  context.fillStyle = "red";
  context.fillRect(0, 0, width, height);
  function draw() {
    analyser.getByteFrequencyData(dataArray);

    for (let x = 0; x < width; x++) {
      const value = dataArray[Math.floor((x / width) * bufferLength)];
      for (let y = 0; y < (value / 255) * height; y++) {
        const index = (x + (height - y - 1) * width) * 4;
        imageData.data[index] = value;
        imageData.data[index + 1] = value;
        imageData.data[index + 2] = value;
        imageData.data[index + 3] = 255;
      }
    }
    context.putImageData(imageData, 0, 0);

    // Request the next animation frame
    requestAnimationFrame(draw);
  }

  // Start drawing the spectrogram
  draw();
}

async function performASR(audio) {
  const recognizer = speechCommands.create("BROWSER_FFT");
  await recognizer.ensureModelLoaded();

  const spectrogram = recognizer.createSpectrogram(audio);
  const inputBuffer = spectrogram.data;

  // Load the TensorFlow.js model
  const model = await tf.loadLayersModel("model.json");

  // Preprocess the input data
  const inputTensor = tf
    .tensor(inputBuffer)
    .reshape([1, ...inputBuffer.shape])
    .div(255.0);

  // Make predictions using the model
  const outputTensor = model.predict(inputTensor);
  const outputData = await outputTensor.data();

  // Decode the predicted output
  const labels = recognizer.wordLabels();
  const index = outputData.indexOf(Math.max(...outputData));
  const predictedWord = labels[index];
console.log(predictedWord)
  return predictedWord;
}
