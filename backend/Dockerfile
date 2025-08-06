FROM python:3.14.0rc1-alpine3.22

WORKDIR /archie

ADD . .

RUN pip install -r requirements.txt && \
    apk add --no-cache curl

EXPOSE 3000

CMD ["python", "app.py"]