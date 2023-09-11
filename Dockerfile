#syntax=docker/dockerfile:1
FROM debian:12
COPY . /app
WORKDIR /app
RUN apt apt update
RUN apt install -y python3
RUN pip install -r requirements.txt
RUN rm -r -f $HOME/.cache
CMD python3 src/main.py
#docker run -v /Llama2-etc:/Llama2-etc
