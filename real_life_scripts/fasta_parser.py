#!/usr/bin/env python3

import sys

fasta_input = sys.argv[1]

fasta_dict = {}


with open(fasta_input, 'r') as fasta:
	for line in fasta:
		line = line.rstrip()
		if line.startswith('>'):
			line = line.strip('>')
			name = line
			fasta_dict[name] = ''
		else:
			fasta_dict[name] += line
print(fasta_dict)			
