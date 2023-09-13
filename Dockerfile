#syntax=docker/dockerfile:1
FROM nvidia/cuda:12.2.0-runtime-ubuntu20.04
COPY . /app
WORKDIR /app
RUN apt update
RUN apt install -y python3 python3-venv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -r requirements.txt
RUN rm -r -f $HOME/.cache
CMD python3 src/main.py
#docker run -v /Llama2-etc:/Llama2-etc
