# Use the official Python image.
FROM python:3.12-slim

# Set the working directory to /backend
WORKDIR /backend

# Copy the current directory contents into the container at /backend
COPY backend /backend

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8080

# Define environment variable


# Run app.py when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
