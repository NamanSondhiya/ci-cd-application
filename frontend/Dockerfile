FROM python:3.15.0a1-alpine3.22

WORKDIR /archie

ADD . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]