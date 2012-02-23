#!/usr/local/bin/python3
"""Validate user input"""

valid_inputs = ['yes', 'no', 'maybe', 'puck you']
input_query_string = 'Type %s: ' % ' or '.join(valid_inputs)
while True:
	s = input(input_query_string)
	if s in valid_inputs:
		break
	print("Wrong! Try again.")
print(s)