#!/usr/bin/env python3
def format_dna(dna, line_length=60):
    # Remove newlines and spaces in the input DNA string
    dna = dna.replace('\n', '').replace(' ', '')
    
    # Break the DNA into chunks of specified length
    formatted_dna = '\n'.join(dna[i:i+line_length] for i in range(0, len(dna), line_length))
    
    return formatted_dna

# Example usage
dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
formatted_dna = format_dna(dna)
print(formatted_dna)

formatted_dna = format_dna(dna, line_length=80)
print(formatted_dna)

def gc_content(dna):
    dna = dna.replace('\n', '').replace(' ', '')
    gc_count = dna.count('G') + dna.count('C')
    return (gc_count / len(dna)) * 100

# Example usage
percent_gc = gc_content('CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA')
print(f"GC content: {percent_gc:.2f}%")

def get_reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_complement = ''.join(complement[base] for base in reversed(dna))
    return reverse_complement

# Example usage
revComp_sequence = get_reverse_complement('CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA')
print(revComp_sequence)

import subprocess

def run_pipeline(command1, command2):
    result1 = subprocess.run(command1, shell=True)
    if result1.returncode == 0:
        print(f"First command executed successfully.")
        result2 = subprocess.run(command2, shell=True)
        if result2.returncode == 0:
            print(f"Second command executed successfully.")
        else:
            print(f"Second command failed with exit code {result2.returncode}")
    else:
        print(f"First command failed with exit code {result1.returncode}")

# Example usage
run_pipeline("echo 'Running first command'", "echo 'Running second command'")
