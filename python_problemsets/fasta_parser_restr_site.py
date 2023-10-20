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


##Grabbing all the cut sites and putting them start and end in a list of lists
rs = []
count = 0
for key in fasta_dict:
	for found in re.finditer(r'[AG]AATT[CT]', fasta_dict[key]):
		seq = found.group(0)
		rs.append([seq])
		rs[count].append(found.start())	
		rs[count].append(found.end())
		count += 1

##Adding the '^' to the cut site in the fasta sequences

for key in fasta_dict:
	fasta_dict[key] = re.sub(r'([AG])(AATT[CT])',r'\1^\2' , fasta_dict[key])

##Separating all the sequences at '^' then storing the fragments in lists

fragmentDict = {}
for key in fasta_dict:
	fragmentDict[key] = fasta_dict[key].split('^')
print(fragmentDict)
	
	
