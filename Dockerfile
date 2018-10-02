FROM python:2-slim

RUN mkdir /app

WORKDIR /app

ADD concoction.py  /app
ADD ingredients.py /app
ADD main.py        /app

EXPOSE 80

CMD python main.py -p 80
