#!/usr/bin/python3

import re

with open('day4part1_input.txt') as f: #'day4part1_input.txt' contains the input
	lines = f.readlines()

sectorIDsum = 0

for line in lines:
	#Save the encrypted name to a variable. Remove the hyphens.
	encryptedNameLetters = re.sub('\d.*','',line)
	encryptedNameLetters = re.sub('-','',encryptedNameLetters)
	encryptedNameLetters = encryptedNameLetters.rstrip()

	#Save the frequency of each letter and its frequency in a 2D list
	letterFreq = []
	for letter in 'abcdefghijklmnopqrstuvwxyz':
		letterFreq.append([letter, 0])

	for letter in encryptedNameLetters:
		letterFreq[ord(letter)-97][1] += 1

	#Sort the 2D list with a bubble sort algorithm
	#Sort the list in order of highest to lowest frequency
	#Letters with the same frequency are sorted alphabetically
	while True:
		numSwaps = 0
		i = 0
		while (i < len(letterFreq)-1):
			#Sort the list in order of highest to lowest frequency
			if letterFreq[i][1] < letterFreq[i+1][1]: 
				temp = letterFreq[i]
				letterFreq[i] = letterFreq[i+1]
				letterFreq[i+1] = temp
				numSwaps += 1

			#Letters with the same frequency are sorted alphabetically
			if letterFreq[i][1] == letterFreq[i+1][1] and letterFreq[i][0] > letterFreq[i+1][0]: 
				temp = letterFreq[i]
				letterFreq[i] = letterFreq[i+1]
				letterFreq[i+1] = temp
				numSwaps += 1

			i += 1
		if numSwaps == 0:
			break

	#Find what the checksum should be
	i = 0
	checksumLetters = []
	while (i < 5):
		checksumLetters.append(letterFreq[i][0])
		i += 1
	calculatedChecksum = ''.join(checksumLetters)
	
	#Extract the given checksum
	givenChecksum = re.sub('.*\[','',line)
	givenChecksum = re.sub('\]', '', givenChecksum)
	givenChecksum = givenChecksum.rstrip()

	#If the given checksum matches what it should be, get the sector ID and increment it to the total
	if calculatedChecksum == givenChecksum:
		sectorID = re.sub('\D','',line)
		sectorIDsum += int(sectorID)

print("The sum of the sector IDs is: " + str(sectorIDsum))