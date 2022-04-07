FROM alpine:latest

RUN apk update

RUN apk add py-pip

RUN apk add --no-cache python3-dev 

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8083

CMD ["python3", "app.py"]