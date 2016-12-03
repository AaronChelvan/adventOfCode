#!/usr/bin/python

with open('day3part1_input.txt') as f: #'day3part1_input.txt' contains the input
    lines = f.readlines()

numPossibleTriangles = 0

for line in lines:
	numbers = line.split() #split the line across any whitespace 
	
	if int(numbers[0]) + int(numbers[1]) > int(numbers[2]) and \
		int(numbers[1]) + int(numbers[2]) > int(numbers[0]) and \
		int(numbers[0]) + int(numbers[2]) > int(numbers[1]):
		numPossibleTriangles += 1

print("Number of possible triangles = " + str(numPossibleTriangles))