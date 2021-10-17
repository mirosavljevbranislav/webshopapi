FROM python:3.7

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]