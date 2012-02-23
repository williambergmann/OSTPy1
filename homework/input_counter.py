#!/usr/local/bin/python3
"""Displays a list of words from input in the order the were entered."""

new_words = set()
words_length = len(new_words)
words_order = {}

while 1:
	text = input("Enter text: ")
	if text == "":
		break
	for punc in ",?;.":
		text = text.replace(punc, "")
	for word in text.lower().split():
		new_words.add(word)
		if len(new_words) > words_length:
			words_length = len(new_words)
			words_order[word] = words_length
	for key in words_order:
		print(key, words_order[key])	
print("Finished")