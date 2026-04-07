FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir fastapi uvicorn pydantic
EXPOSE 8080
CMD ["python", "inference.py"]

