#!/bin/bash
if [ ! -e /usr/bin/python3 ];then
   echo 'Error: python3 is not installed.'
fi
wget https://github.com/telzhou618/x-tools/releases/download/v0.1/x-tools-0.1.tar.gz
pip3 install x-tools-0.1.tar.gz
x-tools