#!/bin/bash
python3 setup.py sdist
cd dist
pip3 install x-tools-0.1.tar.gz
x-tools
