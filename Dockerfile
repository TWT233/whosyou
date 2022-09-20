FROM python:3.10

WORKDIR /home

RUN mkdir whosyou
COPY . whosyou

WORKDIR whosyou

RUN pip install -r requirements.txt

COPY config.yaml config.yaml

CMD python main.py