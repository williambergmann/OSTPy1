#!/usr/local/bin/python3
#
# check_string.py
#
"""This program asks the user to input a string and tests that the string is
all in upper case and ends in a period. If the tests fail, it prints error
messages and if they pass, it prints an indication of success."""

user_string = input("Please input an upper-case string ending in a period: ")

if not user_string.isupper():
	print("Input is not all upper-case.")
if not user_string.endswith("."):
	print("Input does not end with a period.")
elif user_string.isupper() and user_string.endswith("."):
	print("Great Job! Input meets both requirements.")

print("\nMaybe your string is just spaces and/or letters?")
#This is the answer to the puzzle allowing just letters and spaces.
if user_string.isalpha() or (" ") in user_string:
	print("Probably, but there might be some other stuff in there too...")
else:
	print("Nope, definitely not. Sorry to get your hopes up.")
	# maybe it's something crazy like a pineapple
	


