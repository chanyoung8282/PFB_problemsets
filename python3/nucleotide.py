#!/usr/bin/var python3
import sys
dna = sys.argv[1]
dna2 = sys.argv[2]
DNA = dna.upper()
pcA = DNA.count('A')
pcT = DNA.count('T')
pcG = DNA.count('G')
pcC = DNA.count('C')

print(f'positive control DNA count A={pcA}, T={pcT}, G={pcG}, C={pcC}')


DNA = dna2.upper()

unA = DNA.count('A')
unT = DNA.count('T')
unG = DNA.count('G')
unC = DNA.count('C')

print(f'unKnown sequence DNA count A = {unA}, T = {unT}, G = {unG}, C = {unC}')



