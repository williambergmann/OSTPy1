#!/usr/local/bin/python3
"""Count the frequency of each word in a text."""

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
freq = {}
for word in text.lower().split():
	freq[word] = freq.get(word, 0)+1
for word in sorted(freq.keys()):
	print(word, freq[word])