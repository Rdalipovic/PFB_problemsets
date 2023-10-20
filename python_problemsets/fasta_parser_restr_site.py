#!/usr/bin/env python3

import sys
import re

fasta = sys.argv[1]

fasta_dict = {}

with open(fasta, 'r') as fasta:
	for line in fasta:
		line = line.rstrip()
		if re.search(r'>', line):
			line = line.strip('>')
			name = line
			fasta_dict[name] = ''
		else:       
			fasta_dict[name] += line

for key in fasta_dict:
	for found in re.finditer(r'[AG]AATT[CT]', fasta_dict[key]):
		print(found.group(0))
		print(found.start())
		print(found.end())
	
