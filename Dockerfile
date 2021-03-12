FROM python:3.7.2-alpine3.8

ENV path="/usr/src/app/"
RUN mkdir -p $path
WORKDIR $path

COPY . $path

CMD ["python","game.py"]
