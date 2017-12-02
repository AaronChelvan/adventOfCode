#!/usr/bin/python3

import re

with open('day4_input.txt') as f: #'day4_input.txt' contains the input
	lines = f.readlines()

for line in lines:
	sectorID = int(re.sub('\D','',line)) #extract the sectorID from the line
	numShifts = sectorID % 26 #the number of times each letter needs to be shifted forward

	encryptedName = re.sub('\d.*','',line)
	encryptedName = encryptedName.rstrip()
	encryptedName = re.sub('-$','',encryptedName)

	decryptedName = []

	for letter in encryptedName:
		if letter == '-':
			decryptedName.append(' ')
		else:
			i = 0
			while i < numShifts:
				if letter == 'z':
					letter = 'a'
				else:
					letter = chr(ord(letter) + 1)
				i += 1
			decryptedName.append(letter)
	decryptedNameString = ''.join(decryptedName)

	if decryptedNameString == "northpole object storage":
		print("SectorID of North Pole Object Storage: " + str(sectorID))
		exit()
	