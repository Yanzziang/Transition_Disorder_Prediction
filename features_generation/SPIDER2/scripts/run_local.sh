#!/bin/bash

########
blastpgp=/usr/local/bin/psiblast
NR=/Users/yzza/uniref50/Uniref
if [ ! -f $blastpgp ]; then echo "blastpgp is not correctly set"; exit 1; fi
if [ ! -f $NR.pal ]; then echo "NR database is required"; exit 1; fi

xdir=$(dirname $0)
if [ $# -lt 1 ]; then
	echo "usage: $0 *"
	echo "required: $1.pssm"
	exit 1
fi

for seq1 in $*; do
	seq_di=$(dirname $1)
	#echo $(basename $seq1 .seq)
	pro1=$(basename $(basename $seq1 .seq) .pssm)
	[ -f $xdir/../ss_file/$pro1.spd3 ] && continue

	if [ ! -f $xdir/../../pssm/$pro1.pssm ]; then
		psiblast -db $NR -num_iterations 3 -num_alignments 1 -num_threads 8 -query $seq_di/$pro1.seq -out_ascii_pssm $xdir/../../pssm/$pro1.pssm > /dev/null
	fi
	#echo $xdir
	$xdir/pred_pssm.py $xdir/../../pssm/$pro1.pssm
	mv $xdir/$pro1.spd3 $xdir/../ss_file/
done
