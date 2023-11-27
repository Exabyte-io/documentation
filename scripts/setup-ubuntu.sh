#!/bin/bash
# requires prior installation of python 3.7 || 3.8 || 3.9 and pip
sudo apt update
sudo apt install -y --no-install-recommends \
    curl \
    git \
    git-lfs
git lfs pull
git submodule update --recursive --init
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi
