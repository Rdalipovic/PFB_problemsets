#!/usr/bin/env python3

taxa = 'sapiens, erectus, neanderthalensis'

species = taxa.split(', ')

#print(sorted(species, key = len))
'''
count = 1 

while count < 101:
	print(count)
	count += 1
print('Done')


factorial = 1000
count = 1

while factorial > 0:
	count = count * factorial
	factorial -= 1
print(count)


dalist = [101,2,15,22,95,33,2,27,72,15,52]
dalist.sort()
even = []
odd = []
for i in dalist:
	print(i)
	if i % 2 == 0:
		even.append(i)
	else:
		odd.append(i)

print(f'Sum of even numbers: {sum(even)}')
print(f'Sum of odd numbers: {sum(odd)}')


for i in range(1,101):
	print(i)
darange = [i for i in range(1,101)]
print(darange)		

import sys

start = int(sys.argv[1])
end = int(sys.argv[2])+1
for i in range(start,end):
	if i % 2 != 0:
		print(i)

sequences = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
count = 0
for seq in sequences:
	print(count,len(seq),seq, sep = '\t')
	count += 1
'''

sequences = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','TGGGCCC']
tuple_list = [(len(seq),seq) for seq in sequences]
print(tuple_list)
