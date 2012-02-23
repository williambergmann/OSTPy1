#!/usr/local/bin/python3
"""Count the number of different words in a text."""

text = """\
Baa, baa, black sheep,
Have you any wool?
Yes sir, yes sir,
Three bags full;
One for the master,
And one for the dame,
And one for the little boy
Who lives down the lane."""

for punc in ",?;.":
	text = text.replace(punc, "")
print(text)
words = set(text.lower().split())
print("There are", len(words), "distinct words in the text.")