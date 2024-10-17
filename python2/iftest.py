#!/usr/bin/env python3
import sys
number = float(sys.argv[1])

if number > 0:
	print('Positive')
	if number < 50:
		print('it is smaller than 50')
		if number % 2 == 0:
			print('it is an even number that is smaller than 50')
	elif number > 50:
		print('it is larger than 50')
		if number % 3 == 0:
			print('it is larger than 50 and divisible by 3')
	else:
		print('number must be 50')
elif number == 0:
	print('number must be 0')

else:
	print('Negative')
