# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the server script to the working directory
COPY pythonmath1.py /app/pythonmath1.py

# Install any necessary dependencies
#RUN pip install --no-cache-dir socket pybase64

# Expose the port that the server will listen on
EXPOSE 9900

# Run the server script when the container starts
CMD ["python", "pythonmath1.py"]
