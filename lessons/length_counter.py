#!/usr/local/bin/python3
"""Demonstrating the continue statement."""

while True:
	s = input("Enter a line (or Enter to quit): ")
	if not s:
		break
	if s.startswith("#"):
		continue
	print("Length", len(s))