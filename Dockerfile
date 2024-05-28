# Use the official Python base image
FROM python:3.8

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential autoconf libtool pkg-config

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the app
CMD ["gunicorn", "-b", "0.0.0.0:8000", "api:app"]
