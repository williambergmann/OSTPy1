#!/usr/local/bin/python3
"""Reads a string from the user and prints each word 
beginning with those containing upper-case letters."""

text = input("Input your text: ")
# initialize each list of words
upper_words = []
other_words = []

# iterate through input characters
for word in text.split():
	for char in word:
		if char.isupper():
			upper_words.append(word)
			break
	else:
		other_words.append(word)

# recombine to print
upper_first = upper_words + other_words
for item in upper_first:
	print(item)