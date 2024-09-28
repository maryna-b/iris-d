# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY app/requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the entire app directory into the container
COPY app/ /app
COPY model/ /app/model

# Expose the port on which the Flask app will run
EXPOSE 5000

# Define the entrypoint to run the Flask app
CMD ["python", "app.py"]