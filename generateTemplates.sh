#!/bin/bash

python imgurGrabAlbums.py $1

#xargs -n1 flag
cat ${1}.txt | xargs -n1 python imgur2wp.py
