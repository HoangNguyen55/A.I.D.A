#!/bin/bash

path="$1"

if [ ! -d ".venv" ]; then
    read -p "No virtual environment called '.venv' detected, do you want to start the installation process? [y/n]: " confirm
    [[ "$confirm" == [yY]* ]] || exit 0

    echo "Creating virtual environment"
    python3 -m venv .venv

    source .venv/bin/activate
    echo "Installing dependencies using pip"
    pip install -r requirements.txt
fi

source .venv/bin/activate
python3 -m src.client
