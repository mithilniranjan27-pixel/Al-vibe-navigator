FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn
EXPOSE 8080
CMD ["python", "inference.py"]

