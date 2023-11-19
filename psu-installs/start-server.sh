#!/bin/bash
path="$1"
model_path="$2"
pipeout="/tmp/AIDA_INSTALL_PIPE"

cd $path

echo "Creating virtual environment" > "$pipeout.out"
python3 -m venv .venv || virtualenv -p python3 .venv

source .venv/bin/activate
echo "Installing dependencies using pip"
pip install -r requirements.txt > "$pipeout.out"
touch "/tmp/done"
rm "$pipeout.out"

TRANSFORMERS_CACHE="$(pwd)" python3 -m src.server -m "$model_path" --auto-approve-signup --inference-on-startup -v
