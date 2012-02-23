#!/usr/local/bin/python3
"""Inputs a number from one user for another user to guess"""
import random

max_guesses = 5
secret = random.randint(1, 20)
guess_count = 0

while guess_count < max_guesses:
	guess_count += 1
	# Input error handler
	while True:
		guess = int(input("Guess a number: "))
		if guess <= 20 and guess >= 1:
			break
		else:
			print(guess, "is not between 1 and 20, please try again.")
	if guess == secret:
		print("Correct! The secret number was %i. Great Job!" % secret)
		break
	elif guess < secret:
		print("Guess higher.")
	elif guess > secret:
		print("Guess lower.")
else:
	print("Sorry, the number was ", secret)