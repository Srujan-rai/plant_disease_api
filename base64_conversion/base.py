import base64
import json

# Function to convert an image to Base64 string
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        # Read the image file and encode it as Base64
        base64_image = base64.b64encode(img_file.read()).decode('utf-8')
    return base64_image

# Example usage
if __name__ == "__main__":
    image_path = "tomato.jpeg"  # Replace with the path to your image file
    base64_string = image_to_base64(image_path)
    
    # Create a JSON object with the Base64 image string
    json_data = json.dumps({"image": base64_string})

    print(json_data)
