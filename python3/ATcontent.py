import sys
dna = sys.argv[1]
DNA = dna.upper()

A = DNA.count('A')
T = DNA.count('T')
G = DNA.count('G')
C = DNA.count('C')
total = len(DNA)
AT=A+T
print(f'AT content is {AT/total:.2%}')
