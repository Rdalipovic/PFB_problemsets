#!/usr/bin/env python3
import sys
import re

bionet_input = sys.argv[1]

##Make bionet dict with enzyme names as key and cut sites as values

enzymeDict = {}
count=0
splitList = []
with open(bionet_input, 'r') as bionet:
	for line in bionet:
		line = line.rstrip()
		if count < 10:
			count += 1
			#DEATH
		else:
			key, value = re.split(r'\s\s+', line)
			if '^' in value:
				enzymeDict[key] = value

fasta_input = sys.argv[2]
fastaDict = {}

##Import given fasta and make a dict with seqID as key and sequence as value

with open(fasta_input, 'r') as fasta:
	for line in fasta:
		line = line.rstrip()
		if re.search(r'>', line):
			line = line.strip('>')
			name = line
			fastaDict[name] = ''
		else:
			fastaDict[name] += line

## Make a dictionary that has the enzyme name as the key and the specific regular expression for each of the cut sites
reEzDict = {}
for ez in enzymeDict:
	reEzDict[ez] = '('
	for char in enzymeDict[ez]:
		if char == 'C':
			reEzDict[ez] += char
		elif char == 'G':
			reEzDict[ez] += char
		elif char == 'A':
			reEzDict[ez] += char
		elif char == 'T':
			reEzDict[ez] += char
		elif char == '^':
			reEzDict[ez] += ')('
		elif char == 'N':
			reEzDict[ez] += '[ATGC]'
		elif char == 'Y':
			reEzDict[ez] += '[CT]'
		elif char == 'R':
			reEzDict[ez] += '[AG]'
		elif char == 'K':
			reEzDict[ez] += '[GT]'
		elif char == 'M':
			reEzDict[ez] += '[AC]'
		elif char == 'S':
			reEzDict[ez] += '[GC]'
		elif char == 'W':
			reEzDict[ez] += '[AT]'
		elif char == 'B':
			reEzDict[ez] += '[GTC]'
		elif char == 'D':
			reEzDict[ez] += '[GAT]'
		elif char == 'H':
			reEzDict[ez] += '[ACT]'
		elif char == 'V':
			reEzDict[ez] += '[GCA]'
	reEzDict[ez] += ')'

for key in fastaDict:
	seq = fastaDict[key]
	for ez in reEzDict:
		if len(re.findall(reEzDict[ez], seq)) > 0:
			cut_seq = re.sub(rf'{reEzDict[ez]}',r'\1^\2' , seq)
			fragment_list = cut_seq.split('^')
		
			frag_max = max([len(x) for x in fragment_list])
			frag_min = min([len(x) for x in fragment_list])
			avg_length = sum([len(x) for x in fragment_list])/len(fragment_list)
			print(f' Sequence ID: {key}\n Enzyme Name: {ez}\n Number of Fragments: {len(fragment_list)}\n Average fragment length: {avg_length}\n Max Fragment Length: {frag_max}\n Min Fragment Length: {frag_min}\n')



		
			
					




