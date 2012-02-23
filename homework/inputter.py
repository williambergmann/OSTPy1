#!/usr/local/bin/python3
"""Takes user input, saves it to a file, then prints it."""

string_input = "Enter text: "

if output:
    output = open('inputter.txt','r')
    print(output) # print what's already been entered first
else:
    output = open('inputter.txt','a')
output.close()

while True:
    inputter = input(string_input)
    if not inputter:
        break
    output.open('inputter.txt','a')
    output.write(inputter) # append new input
    output.close()