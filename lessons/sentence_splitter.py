#!/usr/local/bin/python3
"""Program to split a sentence into words."""

s = input("Please enter a sentence: ")
while True:
	while s.startswith(" ") or s.startswith("\t"):
		s = s[1:]
	pos = 0
	for c in s:
		if c == " " or c == "\t":
			print(s[:pos])
			s = s[pos+1:]
			break
		pos += 1
	else:
		print(s)
		break