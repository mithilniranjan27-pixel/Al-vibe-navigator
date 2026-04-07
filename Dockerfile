# 1. Use a lightweight Python image
FROM python:3.10-slim

# 2. Set the directory inside the container
WORKDIR /app

# 3. Copy your files (inference.py and requirements.txt) into the container
COPY . .

# 4. Install the necessary libraries (fastapi, uvicorn)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Open port 8080 so the Scaler validator can connect
EXPOSE 8080

# 6. Start the FastAPI server
CMD ["python", "inference.py"]

