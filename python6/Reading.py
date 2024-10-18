#!/usr/bin/env python3
upper = ''
with open('Python_06.txt', 'r') as seq_file_obj, open('Python_06_uc.txt', 'w') as seq_write:

    for line in seq_file_obj:
        line = line.rstrip()
        print(line)
        upper = line.upper()
        seq_write.write(f"{upper}\n") #back slash!
print(upper)
print(seq_write)