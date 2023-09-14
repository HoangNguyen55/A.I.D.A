#syntax=docker/dockerfile:1
# CUDA VERSION MUST MATCH THE HOST
FROM nvidia/cuda:12.2.0-runtime-ubuntu20.04
COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install -y \
python3 \
python3-venv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV TRANSFORMERS_OFFLINE=1
ENV HF_DATASETS_OFFLINE=1

RUN pip install -r requirements.txt
RUN rm -r -f $HOME/.cache
# CMD python3 src/main.py
#docker run -v ~/Llama-2-7b-chat-hf:/Llama-2-7b-chat-hf --gpus all -it <name> /bin/bash
