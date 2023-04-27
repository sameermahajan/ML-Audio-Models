let mediaRecorder;
let chunks = [];

const recordButton = document.getElementById('recordButton');
const stopButton = document.getElementById('stopButton');
const playButton = document.getElementById('playButton');

recordButton.addEventListener('click', startRecording);
stopButton.addEventListener('click', stopRecording);
playButton.addEventListener('click', playRecording);

function startRecording() {
	chunks = [];
	navigator.mediaDevices.getUserMedia({audio: true})
	  .then(stream => {
	    mediaRecorder = new MediaRecorder(stream);
	    mediaRecorder.start();
      
	    recordButton.style.backgroundColor = 'red';
	    stopButton.disabled = false;
	    playButton.disabled = true;
      
	  });
      
	mediaRecorder.addEventListener('dataavailable', event => {
	  chunks.push(event.data);
	});
      }
      
function stopRecording() {
	mediaRecorder.stop();
	mediaRecorder.addEventListener('dataavailable', event => {
	chunks.push(event.data);
});

recordButton.style.backgroundColor = '';
	stopButton.disabled = true;
	playButton.disabled = false;
	createSpectrogram(chunks); // call to createSpectrogram with audio as argument 
}

const audio = new Audio();
audio.controls = true;
document.body.appendChild(audio);

function playRecording() {
	const blob = new Blob(chunks, { type: 'audio/ogg; codecs=opus' });
	const audioURL = URL.createObjectURL(blob);
	audio.src = audioURL;
	audio.play();
}


mediaRecorder.addEventListener('stop', event => {
	const audioBlob = new Blob(chunks, { type: 'audio/ogg; codecs=opus' });
	const audioURL = URL.createObjectURL(audioBlob);
	const audio = new Audio(audioURL);
	audio.controls = true;
	document.body.appendChild(audio);
	audio.play();
	chunks = [];
});
function createSpectrogram(chunks) {
}
