#!/usr/local/bin/python3
"""
Reads a line of input from the user and encodes it taking each character of the
string, making the corresponding character in the output string 1 more than the 
ordinal value of the input, then reversing the text.
"""
message = input("Message: ")
encipher = []

for c in message:
    encipher.append(ord(c)+1)
for i in reversed(encipher):
    print(chr(i), end = '')
print()