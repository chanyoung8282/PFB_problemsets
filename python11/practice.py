#!/usr/bin/env python3
class DNARecord(object):

    def __init__(self, sequence, gene_name, organism ):
        self.sequence = sequence
        self.gene_name = gene_name
        self.organism = organism
    
    def sequence_length(self):
        length = len(self.sequence)
        return length
    
    def nt_composition(self):
        count_sequence = self.sequence
        A_count = count_sequence.count('A')
        T_count = count_sequence.count('T')
        G_count = count_sequence.count('G')
        C_count = count_sequence.count('C')
        total = f"A : {A_count}, T : {T_count}, G : {G_count}, C : {C_count}"
        return total
    
    def GC_ratio(self):
        total = len(self.sequence)
        G_count = self.sequence.count('G')
        C_count = self.sequence.count('C')
        GC = (G_count + C_count)/total
        return GC
    

dna_rec_obj = DNARecord('ACTTGTT', 'ABC1', 'xenopus')

for d in [dna_rec_obj]: 
    print(f"name : {d.gene_name}, sequence : {d.sequence}, organism : {d.organism}")
    print(f"sequence length : {d.sequence_length()}")
    print(d.nt_composition())
    print(f"GC_ratio is : {d.GC_ratio():%}")
