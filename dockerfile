# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# Note: Make sure you have a requirements.txt file with all the necessary packages
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=api/api.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run api.py when the container launches
CMD ["flask", "run"]
