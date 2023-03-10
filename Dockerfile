FROM python:3.10.4-alpine3.15

WORKDIR /mypythonapp

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000/tcp

ENV FLASK_ENV=development
ENV FLASK_APP=app.py

COPY . .

CMD ["python", "-m", "flask", "run","--host=0.0.0.0"]


