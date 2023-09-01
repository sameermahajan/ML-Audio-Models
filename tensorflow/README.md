# serving model

On ubuntu machine
- Installing model server package
  + echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | sudo tee /etc/apt/sources.list.d/tensorflow-serving.list && \
  + curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | sudo apt-key add -
  + sudo apt-get update && sudo apt-get install tensorflow-model-server
- export the model using [serve.py](./serve.py)
- tensorflow_model_server --rest_api_port=8501 --model-name=marathi-100 --model_base_path=/mnt/c/ML/Tables/ML-Audio-Models/tensorflow/serve

# querying model
- [query.py](./query.py) for [Querying the REST Endpoint](https://huggingface.co/blog/tf-serving-vision#querying-the-rest-endpoint)
