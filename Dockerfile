FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install gradio

CMD ["python", "app.py"]
