#!/usr/bin/env python3
value = 20
if value >10:
	print('Aye Captain')
else:
	print('Not True')

number = 50

if number > 0:
	print('positive')
	if number < 50:
		print(number,'smaller than 50')
		if (number % 2) == 0:
			print('it is an even number that is smaller than 50')
		else:
			print("it isn't even number that is smaller than 50")
	elif number == 50:
		print('number must be 50')

	else:
		print(number, 'larger than 50')
		if number % 3 == 0:
			print('it is larger than 50 and divisible by 3') 
elif number < 0:
	print('Negative')
else:
	print('must be 0')
