#!/usr/local/bin/python3
"""Simpler program to list the words of a string."""

s = input("Enter your string: ")
words = s.strip().split()
for word in words:
	print(word)
