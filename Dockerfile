FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /env
WORKDIR /env
ADD requirements.txt /env/
RUN pip install -r requirements.txt
COPY . /env/
