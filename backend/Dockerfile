# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port that your app will run on
EXPOSE 8080

# Command to run your app using gunicorn
CMD ["gunicorn", "server:app", "--bind", "0.0.0.0:8080"]
