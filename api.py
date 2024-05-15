import base64
import json
import tensorflow as tf
import numpy as np
from keras.models import load_model     
from keras.applications.vgg19 import preprocess_input
from flask import Flask, jsonify, request

app = Flask(__name__)
model = load_model("best_model.h5")

data_tuple = (
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [
        'Cherry___Powdery_mildew', 'Cherry___healthy',
        'Pepper___Bacterial_spot', 'Pepper___healthy',
        'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
        'Tomato___Bacterial_spot', 'Tomato___Early_blight',
        'Tomato___Late_blight', 'Tomato___Leaf_Mold',
        'Tomato___Septoria_leaf_spot',
        'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
        'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
        'Tomato___healthy'
    ]
)

ref = {index: disease for index, disease in zip(*data_tuple)}

with open('remedies.json', 'r') as remedies_file:
    remedies_data = json.load(remedies_file)


@app.route('/')
def home():
    return "<h1>Send a base64 encoded string of the affected plant leaf photo to '/predit' endpoint</h1>"


@app.route('/predict', methods=['POST'])
def receive_image():
    try:
        base64_image = request.json['image']
        image_data = base64.b64decode(base64_image)
        image = tf.image.decode_image(image_data)
        image = tf.image.resize(image, (256, 256))
        img_array = tf.keras.applications.vgg19.preprocess_input(image)
        img_array = tf.expand_dims(img_array, axis=0)

        prediction_index = np.argmax(model.predict(img_array))
        predicted_disease = ref.get(prediction_index, 'Unknown disease')

        remedy_info = remedies_data.get(predicted_disease, 'No remedy information available')

        return {'result': predicted_disease, 'remedy': remedy_info}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 8000))  # Use the PORT environment variable provided by Render
    app.run(debug=False, host=host, port=port)
