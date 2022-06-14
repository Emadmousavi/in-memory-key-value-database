FROM python:3.9

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
RUN pip install -U pip setuptools wheel ruamel.yaml.clib==0.2.6

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN python setup.py install