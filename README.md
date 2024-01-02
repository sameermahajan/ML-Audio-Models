# ML-Audio-Models

[![Use Case YouTube Video](UseCase.JPG)](https://youtu.be/L3L4mEszzTs)

This repository has code working with various audio models like

- **tensorflow**: this has a CNN trained from scratch using collected audio samples
- **hierachical models**: build two level models for above
- **whisper**: whisper is a speech to text model developed by OpenAI. This folder has code working with a variety of pretrained models, fine tuning them with your own audio samples, creating datasets for your samples, working with hugging face datasets etc.
- **speech_recognition**: speech_recognition is a python package. It is a speech to text model using Google APIs
- **wave2vec2_xlsr_marathi_model**
- **Shazam**
- **samples**: folder has audio recordings of numbers 1 through 40 in marathi
- **working_with_wav_files**: folder has handy snippets of python code required for processing of wav files
- **misc**: folder has miscellaneous handy code developed during the project

[![Blog on Medium](blog.JPG)](https://sameermahajan.medium.com/ml-working-with-audio-data-34b296d3e413)

## Current Project Status

We came across speech commands model (tensor flow CNN). It has reasonable accuracy over 90% for numbers 1 through 100.

To improve the accuracy further we tried to train hierarchical models. Thanks [Harshad Nanal](https://github.com/hniot) for the suggestion. One of the approaches was a 'tens' model and 'units' models (10 of them namely for 1-10, 11-20, ..., 91-100). Then run the inferencing through the tens model and qualified units model (only one so overall running through only two models). As the number of classes for each model are limited to 10, we might get better model wise and eventually overall accuracy. Another approach was to use vertical and horizontal models as:
vertical:- label names: \['1-18' '19-28' '29-38'\]
classification:- 1-18 and
horizontal
label names: \['19-99' '20-100' '21-91' '22-92' '23-93' '24-94' '25-95' '26-96' '27-97' '28-98'\]

[This approach](https://www.kaggle.com/code/christianlillelund/classify-mnist-audio-using-spectrograms-keras-cnn/notebook#Modelling) seems even better.

We came across whisper model of "DrishtiSharma/whisper-large-v2-marathi" which is reasonable but it is rather large over 6 GB to fit in an android app.

We explored google recognition / speech_recognition but it needs internet / online connection.

We have put together a [kivy app](https://github.com/sameermahajan/PaadasML) having integration with google speech recognition that you can try out.

We have put together a [flask web app](https://github.com/sameermahajan/PaadasMLFlaskApp) again having integration with google speech recognition that also you can try out. We are looking to host it so that you can try it out directly and will share its link here once done.

We have also put together a [Kivy android app](https://github.com/sameermahajan/Paadas) that can work in conjunction with Marathi voice keyboard(s) though it is [not a very seamless experience](https://youtube.com/shorts/Gfeo_Dyakoc). Also these voice keyboards need internet / online connection and might not be all that great. We think underneath they might anyway be using something like google speech recognition / speech_recognition that we have explored and mentioned above.

We are also exploring wave2vec2_xlsr_marathi_model which is just over 1 GB but need to test further.

We also tried [Shazam](https://www.toptal.com/algorithms/shazam-it-music-processing-fingerprinting-and-recognition) Thanks [Chiradeep](https://github.com/chiradeep) for the suggestion. However when we tried [finger printing](https://github.com/worldveil/dejavu) on our recorded audio samples (about 50 per number), for a few numbers, the fingerprints were totally different for different samples of the same number. It makes us believe that this approach also won't work in our case. It could be due to the difference in our use case of
- just vocal and no instruments causing different, may be narrower frequency spread
- short samples of about 3-4 seconds meaning no multi fingerprint checkpoints for the same sample for comparison
- uncotrolled varied recording conditions unlike songs etc.

## Current Plan

With above findings, we are going to
-  Add some [UI](https://youtu.be/LAKjpql5sHs). You can interact with our [hosted flask app version](https://paadas-flask-app.onrender.com/) for its look and feel (bear its speech recognition which is currently way off).
-  Build a lightweight small footprint offline version of our [PaadasML](https://github.com/sameermahajan/Paadas) android app to reach masses having devices with small memory, disk and poor network connectivity based on this model.
- Improve accuracy of this model as determined by field trials of the app.
- Put out [PaadasML](https://github.com/sameermahajan/PaadasML) and / or [PaadasMLFlaskApp](https://github.com/sameermahajan/PaadasMLFlaskApp) for feedback and audio sample collection
- Train tensoflow model with more data (as collected above) and possibly improve the model as RNN, LSTM, more layers etc.

## Some Additional Contributions from the project

### Datasets
- [Marathi Numbers 1-20](https://huggingface.co/datasets/SameerMahajan/marathi_numbers-1-20)
- [Marathi Numbers 1-40](https://huggingface.co/datasets/SameerMahajan/marathi_numbers-1-40)

### Models
- [Tensorflow Audio Model for marathi numbers 1 through 40](https://tfhub.dev/sameermahajan/marathi-numbers-1-40/1)
- [Tensorflow Audio Model for 100 marathi numbers](https://tfhub.dev/sameermahajan/marathi-numbers-1-100/1)
- 
## Issue Deploying pyaudio package on android (ARM)

For using SpeechRecognition package we need pyaudio package. To bundle it in an apk (to deploy and use it on android), it needs to be installed using pip.
There are 3 ways (local linux, google colab, GitHub action) for deploying python apps on android as detailed in https://towardsdatascience.com/3-ways-to-convert-python-app-into-apk-77f4c9cd55af

I tried all three options without any luck. I run into the exact same error on all the systems i.e.

```
/usr/include/limits.h:26:10: fatal error: 'bits/libc-header-start.h' file not found
34939  #include <bits/libc-header-start.h>
34940           ^~~~~~~~~~~~~~~~~~~~~~~~~~
34941  1 error generated.
34942  error: command '/usr/bin/ccache' failed with exit code 1
34943  error: subprocess-exited-with-error
34944  
34945  × Building wheel for pyaudio (pyproject.toml) did not run successfully.
34946  │ exit code: 1
ERROR: Failed building wheel for pyaudio
34954Failed to build pyaudio
34955ERROR: Could not build wheels for pyaudio, which is required to install pyproject.toml-based projects
```

which I am still not able to get around. I think the problem is with cross compilation since all these systems are x86_64 Ubuntu and we want to build the apk for ARM. I could build x86_64 based apk on my local system however it doesn't work on most phones :( One option is to get hold of an ARM system (don't know how to do that :() and try a build there.

I also explored options of python for android and kivy launcher without luck.

Jumping on ChatGPT bandwagon, I also converted this kivy app into react native. We are currently exploring whether we can build it into an android apk using studio.
