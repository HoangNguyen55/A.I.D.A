#!/bin/bash

path="$1"

cd $path
source .venv/bin/activate
python3 -m src.client "$@"
