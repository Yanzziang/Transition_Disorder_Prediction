#!/bin/bash

filelist=`ls /usr/disorder-dataset/`

for file in $filelist
do
    python3 /usr/disorder-dataset/phschem/phsicochemical.py /usr/disorder-dataset/$file
done
