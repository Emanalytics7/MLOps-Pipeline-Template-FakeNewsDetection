# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Set environment variables:
# - Prevent Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# - Prevent Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies:
# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/
# Install the Python dependencies from requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the local directory contents into the container at /app
COPY . /app

# Make port 5300 available to the world outside this container
EXPOSE 5300

# Define environment variable to store where the model and other data files will be mounted
ENV MODEL_DIR=/app/models

# Create a directory where the model file will be saved
RUN mkdir -p ${MODEL_DIR}

# Run app.py when the container launches
CMD ["python", "main.py"]
