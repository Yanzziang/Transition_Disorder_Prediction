#!/bin/bash

########
blastpgp=~/work/blast/ncbi-blast-2.7.1+/bin/psiblast
NR=~/work/Database/uniref_3/uniref_3
if [ ! -f $blastpgp ]; then echo "psiblast is not correctly set"; exit 1; fi
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
	pro1=$(basename $(basename $seq1 .fasta) .pssm)

	if [ ! -f $xdir/../../pssm/$pro1.pssm ]; then
		$blastpgp -db $NR -num_iterations 3 -num_alignments 1 -num_threads 8 -query $seq_di/$pro1.fasta -out_ascii_pssm $xdir/../../pssm/$pro1.pssm > /dev/null
	fi
	#echo $xdir
	$xdir/pred_pssm.py $xdir/../../pssm/$pro1.pssm
	mv $xdir/../$pro1.spd3 $xdir/../ss_file/
done
