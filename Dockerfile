FROM python:3.8.5

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 0
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN python setup.py install
