import base64
import json
import requests
import sys
import tensorflow as tf

x = tf.io.read_file(sys.argv[1])
b64str = base64.urlsafe_b64encode(x.numpy()).decode("utf-8")

data = json.dumps({"signature_name": "serving_default", "instances": [b64str]})

headers = {"content-type": "application/json"}
json_response = requests.post(
            "http://localhost:8501/v1/models/default/versions/1:predict", data=data, headers=headers
            )
#print(json.loads(json_response.text))

import numpy as np
print(np.argmax(np.array((json.loads(json_response.text)["predictions"][0]))))
