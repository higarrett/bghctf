# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and requirements.txt file into the container
COPY network1.py /app/network1.py
COPY requirements.txt /app/

# Install the Python dependencies (none in this case)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the server will listen on
EXPOSE 9910

# Run the Python script when the container starts
CMD ["python", "network1.py"]

