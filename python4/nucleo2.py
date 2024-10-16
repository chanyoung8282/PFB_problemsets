nt = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
nt_list = []

for dna in nt:
	nt_list.append((nt.index(dna),len(dna),dna))
print(nt_list)
