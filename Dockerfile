# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt requirements.txt

# Upgrade pip and install dependencies with a custom timeout and alternative index
RUN pip install --upgrade pip && \
    pip install --default-timeout=100 -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 80

# Define environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
