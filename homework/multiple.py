#!/usr/local/bin/python3
""" Takes a tuple of two-element tuples and prints 
the result of multiplying each pair together"""

pairs = ((2,3),(45,23),(12,7),(2,28),(0,14))

for pair in pairs:
	product = pair[0]*pair[1]	
	print("{0:5} = {1:2} x {2:2}".format(product, pair[0], pair[1]))