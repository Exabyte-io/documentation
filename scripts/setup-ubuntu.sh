#!/bin/bash
sudo apt update
sudo apt install -y --no-install-recommends \
    git \
    git-lfs \
    python2.7 \
    python-pip
pip2 install virtualenv
if [ -f requirements.txt ]; then
    pip2 install -r requirements.txt
fi
git submodule update --recursive --init
