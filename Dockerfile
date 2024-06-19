# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables, including TRANSFORMERS_CACHE
ENV TRANSFORMERS_CACHE /app/cache

# Set cache directory permissions
RUN mkdir -p /app/cache && chmod 777 /app/cache

# Make port 7860 available to the world outside this container
EXPOSE 7860

# Define the command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
