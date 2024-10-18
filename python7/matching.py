import re
scripts = ''
gene = {}

with open('Python_07.fasta.txt', 'r') as script:
    for line in script:
        line = line.rstrip()
        for match in re.finditer(r"(>\S*)\s(.*)", line):
            id = match.group(1)
            desc = match.group(2)
            gene[id] = desc
            #print(f"id: {gene.keys()} desc: {gene.values}")

#print(gene)

for genes in gene:
    desc = gene[genes]
    print(f"id: {genes}, desc: {desc}")