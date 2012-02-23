#!/usr/local/bin/python3
"""Takes user input, saves it to a file, then prints it."""

string_input = "Enter text: "

f = open('inputter.txt','a')
f.close()

f = open('inputter.txt','r')
print(f.read()) # print what's already been entered first
f.close()

while True:
    inputter = input(string_input)
    if not inputter:
        break
    
    f = open('inputter.txt','a')
    f.write(inputter) # append new input
    f.close()

    f = open('inputter.txt','r')
    print(f.read()) # print new input
    f.close()