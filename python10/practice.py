#!/usr/bin/env python3

def gc_content(dna='N'):
    c_count = dna.count('C')
    g_count = dna.count('G')
    dna_len = len(dna)
    output_count = (c_count + g_count) / dna_len
    return output_count

def get_first_codon(dna):
    return dna[0:3]

dna_string = "GTACCTTGATTTCGTATTCTGAGAGGCTGCT"
#print(gc_content(dna_string))
#dna_gc = gc_content("GTACCTTGATTTCGTATTCTGAGAGGCTGCT")
#print(dna_gc)
#print(gc_content(dna=dna_string))
#print(gc_content())

#print(get_first_codon(dna_string))
import subprocess
#subprocess.run(['ls','-l'])
output = subprocess.check_output('ls -l | grep pfb2024', shell = True)
print(output)
