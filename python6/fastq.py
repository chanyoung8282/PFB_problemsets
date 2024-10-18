#!/usr/bin/env python3

total_number_line = 0
total_number_char = 0
with open('Python_06.fastq.txt', 'r') as seq_file_obj:
    for line in seq_file_obj:
        line.rstrip()
        total_number_line += 1
        count = len(line)
        total_number_char += count
        #count()

print(total_number_line)
print(total_number_char) 
print(total_number_char/total_number_line)