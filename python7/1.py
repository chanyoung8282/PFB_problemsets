#!/usr/bin/env python3
import re
scripts = ''
with open('Python_07_nobody.txt', 'r') as script:
    for line in script:
        line.rstrip()
        scripts += line
#print(scripts)

#for match in re.finditer(r"Nobody",scripts):
#    print(match)

new_scripts =''

for match in scripts:
    new_scripts = re.sub(r"Nobody", 'friends', scripts)

print(new_scripts)

#print(scripts)
#nobody = re.search(r"Nobody",scripts)
#print(nobody)#