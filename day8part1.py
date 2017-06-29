#!/usr/bin/python3

import re

with open('day8_input.txt') as f:
	lines = f.readlines()

#Print the current state of the screen - for debugging purposes
def printScreen(screen):
	for i in range(6):
		print(screen[i])

#Returns the number of lit pixels
def numLitPixels(screen):
	numLit = 0
	for i in range(6):
		for j in range(50):
			if screen[i][j] == 1:
				numLit += 1
	return numLit

#Initialise a 2D list representation of the 50 x 6 screen
#1 = pixel is lit. 0 = pixel is not lit.
screen = [[],[],[],[],[],[]]
for i in range(6):
	for j in range(50):
		screen[i].append(0)

for line in lines:
	if "rect" in line: #if it is a "rect" operation
		#Extract the dimensions of the rectangle
		numbers = re.sub(r'\D', '', line)
		numCols = int(numbers[0])
		numRows = int(numbers[1])

		#Light up the corresponding section of the screen
		for i in range(numRows):
			for j in range(numCols):
				screen[i][j] = 1
		
	elif "row" in line: #if it is a "rotate row" operation
		#Extract the numbers from the line
		numbers = line
		numbers = re.sub(r'\D', '', numbers)
		rowNumber = int(numbers[0])
		amountToRotate = int(numbers[1])
		amountToRotate = amountToRotate % 50

		#Rotate the pixels
		newRow = [0] * 50
		for i in range(50):
			if i < amountToRotate:
				newRow[i] = screen[rowNumber][50 - amountToRotate + i]
			else:
				newRow[i] = screen[rowNumber][i - amountToRotate]

		#Copy over newRow to the screen
		for i in range(50):
			screen[rowNumber][i] = newRow[i]

	elif "column" in line: #if it is a "rotate column" operation
		#Extract the numbers from the line
		numbers = line
		numbers = re.sub(r'\D', '', numbers)
		colNumber = int(numbers[0])
		amountToRotate = int(numbers[1])
		amountToRotate = amountToRotate % 6
		
		#Rotate the pixels
		newCol = [0] * 6
		for i in range(6):
			if i < amountToRotate:
				newCol[i] = screen[6 - amountToRotate + i][colNumber]
			else:
				newCol[i] = screen[i - amountToRotate][colNumber]

		#Copy over newCol to the screen
		for i in range(6):
			screen[i][colNumber] = newCol[i]
	else:
		print("ERROR")
	#printScreen(screen)
	#print(numLitPixels(screen))

print("Number of lit pixels: " + str(numLitPixels(screen)))