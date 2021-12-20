FROM python:3.8-slim-buster
ENV TZ=Asia/Almaty
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY parser_carefood_kz .

CMD [ "python3", "manage.py" ]
