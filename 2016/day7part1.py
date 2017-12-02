#!/usr/bin/python3

import re

with open('day7_input.txt') as f:
	lines = f.readlines()

#Look for the ABBA pattern
numMatches = 0
for line in lines:
	#Extract 2 strings from the line
	#
	#lettersNotInBrackets contains all letters not inside a pair of square brackets
	#letters inside square brackets are removed, but the square brackets [] remain
	#
	#lettersInBrackets contains all letters inside a pair of square brackets
	#letters outside square brackets are removed
	lettersNotInBrackets = re.sub(r'\[\w*\]', '[]', line)
	lettersInBrackets = re.sub(r'\]\w*\[','][', line)
	lettersInBrackets = re.sub(r'\w*\[', '[', lettersInBrackets)
	lettersInBrackets = re.sub(r'\]\w*', ']', lettersInBrackets)

	matchInBrackets = False
	#Look for ABBA pattern in letters inside brackets
	#If found, ignore that line
	for i in range(len(lettersInBrackets)-3):
		if (lettersInBrackets[i] == lettersInBrackets[i+3]) and \
		   (lettersInBrackets[i+1] == lettersInBrackets[i+2]) and \
		   (lettersInBrackets[i] != lettersInBrackets[i+1]):
			matchInBrackets = True
			break
	if matchInBrackets == True:
		continue

	#Look for ABBA pattern in letters outside of brackets
	for i in range(len(lettersNotInBrackets)-3):
		if (lettersNotInBrackets[i] == lettersNotInBrackets[i+3]) and \
		   (lettersNotInBrackets[i+1] == lettersNotInBrackets[i+2]) and \
		   (lettersNotInBrackets[i] != lettersNotInBrackets[i+1]):
			numMatches += 1
			break

print("Number of IPs supporting TLS: " + str(numMatches))