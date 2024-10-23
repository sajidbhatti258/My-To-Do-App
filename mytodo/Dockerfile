# Use the official Python image from Docker Hub
FROM python:3.12.3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local files to the container's /app directory
COPY . .

# Install dependencies from requirements.txt
RUN pip install  -r requirements.txt

# Expose a port if you're running the Django server
EXPOSE 8000

# Run Django's development server on container startup
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
