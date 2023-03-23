# Set the base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the autocarPython.py file to the working directory
COPY autocarPython.py .

# Set the command to run the autocarPython.py script
CMD ["python", "autocarPython.py"]
