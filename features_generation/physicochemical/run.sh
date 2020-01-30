#!/bin/bash

filelist=`ls /Users/yzza/disorder-dataset/`

for file in $filelist
do
    python3 /Users/yzza/disorder-dataset/phschem/phsicochemical.py /Users/yzza/disorder-dataset/$file
done
