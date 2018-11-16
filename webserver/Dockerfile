FROM python:3-slim

RUN mkdir /app

WORKDIR /app

ADD concoction.py  /app
ADD ingredients.py /app
ADD main.py        /app

EXPOSE 80

CMD python concoction_webserver.py -p 80
