#!/bin/bash
sudo apt update
sudo apt install -y --no-install-recommends \
    curl \
    git \
    git-lfs \
    python3 \
    python3-pip
pip install virtualenv
git lfs pull
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi
git submodule update --recursive --init
