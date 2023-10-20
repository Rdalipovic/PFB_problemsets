#!/usr/bin/env python3

import sys


char_count = 0
line_list = []
input_fastq = sys.argv[1]
with open(input_fastq,'r') as fastq_read:
	for line in fastq_read:
		line = line.rstrip()
		char_count += len(line)
		line_list.append(len(line))

print(f'Total number of lines: {len(line_list)}\nTotal character count: {char_count}\n Average line length: {sum(line_list)/len(line_list)}')
