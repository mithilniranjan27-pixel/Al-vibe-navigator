# Use a Python base image
FROM python:3.10-slim

# Set workspace
WORKDIR /app

# Copy all files to the container
COPY . .

# Install dependencies directly to avoid build errors
RUN pip install --no-cache-dir fastapi uvicorn pydantic

# Expose the communication port
EXPOSE 8080

# Execute the script
CMD ["python", "inference.py"]


