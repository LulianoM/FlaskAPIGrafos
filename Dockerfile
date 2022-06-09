FROM python:3.9.5-slim-buster AS builder

ENV LC_ALL "pt_BR.UTF-8"
ENV LC_CTYPE "pt_BR.UTF-8"

RUN apt-get update 

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements/requirements.txt /app
RUN pip install -r requirements.txt

FROM builder AS api
COPY . /app
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "manage:app", "--workers=3", "--threads=5"]
