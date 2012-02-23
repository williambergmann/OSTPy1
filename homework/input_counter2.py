#!/usr/local/bin/python3
"""Displays a list of words in order from input in the actual order the were entered."""

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
	# to output words by their respective order of appearance
	ordered = []
	for key in words_order:
		ordered.append((words_order[key], key))
	for i in sorted(ordered):
		print(i[1], i[0])	
print("Finished")