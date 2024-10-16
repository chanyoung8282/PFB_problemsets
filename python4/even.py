number = [101,2,15,22,95,33,2,27,72,15,52]
sumeven = int(0)
sumodds = int(0)
for even in number:
	if (even%2)==0:
		print(even)
		sumeven = sumeven + even
	else:
		sumodds = sumodds + even

print(f'sum of even number: {sumeven}')
print(f'sum of odds: {sumodds}')
		
		

