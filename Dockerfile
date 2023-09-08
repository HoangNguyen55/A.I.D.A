#syntax=docker/dockerfile:1
FROM debian:12
COPY . /app
RUN make /app
RUN rm -r $HOME/.cache
CMD python /app/src/main.py
#docker run -v /Llama2-etc:/Llama2-etc
