#!/bin/bash

# 
# build the java app with a container
#

set -e 
set -v 

hostname
whoami
pwd

docker run -it --rm \
  -v "$PWD/src":/code \
  -w "/code" \
  bingo \
  /usr/local/bin/python /code/bingo.py

