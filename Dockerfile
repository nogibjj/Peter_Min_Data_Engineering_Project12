FROM python:3.11-slim

WORKDIR /code

COPY . /app

RUN pip3 install -no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]