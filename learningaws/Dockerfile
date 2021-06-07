FROM python:3.8.3
ENV PYTHONUNBUFFERED 1

RUN mkdir /learningaws
WORKDIR /learningaws
COPY requirements.txt /learningaws/
RUN pip install -r requirements.txt
COPY . /learningaws/
COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x docker-entrypoint.sh