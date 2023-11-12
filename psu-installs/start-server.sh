#!/bin/bash
path="$1"
model_path="$2"

cd $path

echo "Creating virtual environment"
python3 -m venv .venv || virtualenv -p python3 .venv

source .venv/bin/activate
echo "Installing dependencies using pip"
pip install -r requirements.txt
touch "/tmp/done"

python3 -m src.server -m "$model_path" --auto-approve-signup --inference-on-startup -v
