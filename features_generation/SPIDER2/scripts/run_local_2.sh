#!/bin/bash

########
xdir=$(dirname $0)
if [ $# -lt 1 ]; then
	echo "usage: $0 *"
	echo "required: $1.pssm"
	exit 1
fi

echo $xdir
$xdir/pred_pssm.py $1
