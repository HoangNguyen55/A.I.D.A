#!/bin/sh
source="$1"
user="$2"

if [ ! -d "$source" ]; then
    echo "Missing path to the folder you want to put inside the machine" >&2
    exit
fi

if [ -z "$user" ]; then
    echo "Missing user (Your Penn state email)" >&2
    exit
fi

rsync -rz --filter=':- .gitignore'  "$source"  "$user@oz-cl-00.oz.psu.edu:~/"
