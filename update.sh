#!/usr/bin/env bash

python topswim.py $1 $2 $3

# update index.html

python update_index.py

# update toc.html

python update_toc.py
