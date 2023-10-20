#!/usr/bin/env python3
import sys
import re

file = sys.argv[1]

enzymeDict = {}
count=0
splitList = []
with open(file, 'r') as bionet:
	for line in bionet:
		line = line.rstrip()
		if count < 10:
			count += 1
			#DEATH
		else:
			key, value = re.split(r'\s\s+', line)
			enzymeDict[key] = value



