#!/usr/bin/python3

import re

with open('day7_input.txt') as f:
	lines = f.readlines()

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

	#Look for BAB pattern in letters inside brackets
	#If found, look for matching ABA pattern in letters outside of brackets
	#If both found, then that line is a match
	matchFound = False
	for i in range(len(lettersInBrackets)-2):
		if (lettersInBrackets[i] == lettersInBrackets[i+2]) and (lettersInBrackets[i] != lettersInBrackets[i+1]):
			#Look for ABA pattern in letters outside of brackets
			for j in range(len(lettersNotInBrackets)-2):
				if (lettersNotInBrackets[j] == lettersNotInBrackets[j+2]) and \
				   (lettersNotInBrackets[j] != lettersNotInBrackets[j+1]) and \
				   (lettersInBrackets[i] == lettersNotInBrackets[j+1]) and \
				   (lettersInBrackets[i+1] == lettersNotInBrackets[j]):
					numMatches += 1
					matchFound = True
					break
			if matchFound == True:
				break

print("Number of IPs supporting SSL: " + str(numMatches))