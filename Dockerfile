FROM python:3.8-slim

COPY . /app

WORKDIR /app

RUN pip install -r /app/requirements.txt

ENV FLASK_APP=app
ENV FLASK_ENV=development

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
