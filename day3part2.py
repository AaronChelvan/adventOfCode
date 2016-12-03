#!/usr/bin/python3

def checkPossibleTriangle (num1, num2, num3):
	if num1 + num2 > num3 and num2 + num3 > num1 and num1 + num3 > num2:
		return 1

with open('day3part1_input.txt') as f: #'day3part1_input.txt' contains the input
    lines = f.readlines()

numPossibleTriangles = 0

#loop over the lines with a step size of 3
for i in range(0,len(lines),3):
	line1numbers = lines[i].split()
	line2numbers = lines[i+1].split()
	line3numbers = lines[i+2].split()
	
	if checkPossibleTriangle(int(line1numbers[0]), int(line2numbers[0]), int(line3numbers[0])):
		numPossibleTriangles += 1
	if checkPossibleTriangle(int(line1numbers[1]), int(line2numbers[1]), int(line3numbers[1])):
		numPossibleTriangles += 1
	if checkPossibleTriangle(int(line1numbers[2]), int(line2numbers[2]), int(line3numbers[2])):
		numPossibleTriangles += 1

print("Number of possible triangles = " + str(numPossibleTriangles))