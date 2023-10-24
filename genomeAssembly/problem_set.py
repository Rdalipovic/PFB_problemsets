#!/usr/bin/env python3
i
from Bio import SeqIO

contigRecords = SeqIO.to_dict(SeqIO.parse("./ecoli_0.25.contigs.fasta", "fasta"))

print(f'Number of contigs: {len(contigRecords)}')
shortestC = 10000000
longestC = 0
for seq in contigRecords:
	if len(contigRecords[seq]) < shortestC:
		shortestC = len(contigRecords[seq])
	elif len(contigRecords[seq]) > longestC:
		longestC = len(contigRecords[seq])

#two ways to do the same thing, second looks more cool
totalContigLen1 = 0
for seq in contigRecords.keys():
	totalContigLen1 += len(contigRecords[seq])

totalContigLen = sum([len(contigRecords[seq]) for seq in contigRecords.keys()])


print(f'Shortest Contig: {shortestC}\nLongest Contig: {longestC}\nTotal Contig Length: {totalContigLen}')
