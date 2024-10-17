#!/usr/bin/env python3
import sys
dna = sys.argv[1]
eco_first = dna.find('GAATTC') + 1
print(eco_first)
eco_end = dna.rfind('GAATTC') + 1
print(eco_end)
