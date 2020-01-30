#!/bin/bash

########
xdir=$(dirname $0)

if [ $# -le 1 ]
then
	$xdir/pred.py $1
else
	echo "It only support one sequence prediction"
fi
