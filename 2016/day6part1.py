#!/usr/bin/python3

#Converts a letter to the corresponding number
#a->0, b->1, ..., z->25
def charToNumber(char):
	return ord(char) - 97

#Converts a number to the corresponding letter
#0->a, 1->b, ..., 25->z
def numberToChar(number):
	return chr(number + 97)

with open('day6_input.txt') as f:
	lines = f.readlines()

answer = []

#Find the most frequent letter in each column
for column in range(len(lines[0])-1):
	
	#An array containing the frequency of each letter. 
	#Index 0 -> a, Index 1 -> b, etc.
	letterFreq = [0]*26 

	#Count the frequencies of each letter
	for line in lines:
		line = line.rstrip()
		letterFreq[charToNumber(line[column])] += 1
	
	#Find the most common letter, by finding the highest value in letterFreq
	mostFreqLetterIndex = 0 #The index of the most frequent letter. 'a' has index 0, 'b' has index 1, etc.
	for i in range(len(letterFreq)):
		if letterFreq[i] > letterFreq[mostFreqLetterIndex]:
			mostFreqLetterIndex = i 
	answer.append(numberToChar(mostFreqLetterIndex))

print("The error-corrected version of the message is: " + "".join(answer))