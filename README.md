# Plant Disease Detection API

Welcome to the Plant Disease Detection API repository! This API utilizes deep learning to predict plant diseases from images, aiding in early disease detection and effective plant health management.

## Overview

The Plant Disease Detection API employs a deep learning model trained on a dataset containing over 7000 images of various plant diseases and healthy plants. The model, built using TensorFlow and Keras, leverages the VGG19 pre-trained model for image processing, enabling accurate disease identification.

## How It Works

1. **Send Image:** Send a base64-encoded image of a plant leaf to the API endpoint.
2. **Processing:** The API processes the image, predicts the disease, and suggests a suitable remedy.
3. **Remedy Suggestions:** Along with disease prediction, the API provides information on remedies fetched from a JSON file.

## Technical Details

- **Framework:** Built using TensorFlow and Keras.
- **Model:** Utilizes the VGG19 pre-trained model for image processing.
- **Remedy Data:** Remedy information is fetched from a JSON file and integrated into the API response.

## Usage

### API Endpoint

The API endpoint for plant disease detection is: [https://plant-disease-api-jxrm.onrender.com](https://plant-disease-api-jxrm.onrender.com)

### Example Request

```bash
curl -X POST \
  https://plant-disease-api-jxrm.onrender.com/predict \
  -H 'Content-Type: application/json' \
  -d '{
    "image": "<base64-encoded image>"
}'
