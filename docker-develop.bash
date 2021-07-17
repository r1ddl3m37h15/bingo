#!/bin/bash

# 
# build the java app with a container
#

set -e 

hostname
whoami
pwd

test -z JOB_NUMBER || JOB_NUMBER=00001

docker run -it \
  -v "$PWD/src":/code \
  -w /code \
  -e JOB_NUMBER=$JOB_NUMBER \
  bingo \
  /bin/bash $*

