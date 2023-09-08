#syntax=docker/dockerfile:1
FROM debian:12
COPY . /app
RUN apt apt update
RUN apt install -y make python3
RUN make /app
RUN rm -r -f $HOME/.cache
CMD python3 /app/src/main.py
#docker run -v /Llama2-etc:/Llama2-etc
