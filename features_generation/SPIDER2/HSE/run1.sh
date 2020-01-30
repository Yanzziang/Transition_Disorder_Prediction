#!/bin/bash

xdir=$(dirname $0)
PSSM_dir=$xdir/../../pssm/

#if [ $# -le 1 ]; then echo "usage: $0  PSSM_dir *.spd3"; exit 1; fi
if [ $# -lt 1 ]; then echo "usage: $0  *.spd3"; exit 1; fi

#PSSM_dir=$1; shift
$xdir/pred_HSE.py $xdir/hsa_full $PSSM_dir NULL $* -hsa
$xdir/pred_HSE.py $xdir/hsb_full $PSSM_dir NULL $* -hsb


mv $xdir/*.hsa2 $xdir/../ss_file/
mv $xdir/*.hsb2 $xdir/../ss_file/
