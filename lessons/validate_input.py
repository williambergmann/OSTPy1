#!/usr/local/bin/python3
"""Validate user input"""

while True:
	s = input("Type 'yes' or 'no':")
	if s == 'yes':
		break
	if s == 'no':
		break
	print("Wrong! Try again.")
print(s)