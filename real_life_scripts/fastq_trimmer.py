#!/usr/bin/env python3

import sys
from Bio import SeqIO

fastq_input = sys.argv[1]
min_qual = int(sys.argv[2])
fastq_output = sys.argv[3]

#for loop that looks at sequences in reverse and removing them based on the min quality input number

output = open(fastq_output, 'w')

for seq_record in SeqIO.parse(fastq_input, "fastq"):
	seqLen = len(seq_record.seq)
	for score in seq_record.letter_annotations["phred_quality"][::-1]:
		if score >= min_qual:
			break
		else:
			seqLen -= 1
	seq_record = seq_record[0:seqLen]	
	output.write(seq_record.format("fastq"))
	
output.close()	
