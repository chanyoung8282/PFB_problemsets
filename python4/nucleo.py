#!/usr/bin/env python3
nt = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']


for dna in nt:
	print(f'{len(dna)}\t{dna}\n')

for dna in nt:
	print(f'{nt.index(dna)}\t{len(dna)}\t{dna}\n')

