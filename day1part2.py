#!/usr/bin/python

import re

#Takes 2 arguments:
#    oldDirection = direction you are currently facing (U/D/L/R)
#    move = the move you made (L/R)
#Returns the new direction you are facing (U/D/L/R)
def newDirection (oldDirection, move):
	if oldDirection == "U":
		if move == "L":
			result = "L"
		elif move == "R":
			result = "R"
	elif oldDirection == "D":
		if move == "L":
			result = "R"
		elif move == "R":
			result = "L"
	elif oldDirection == "L":
		if move == "L":
			result = "D"
		elif move == "R":
			result = "U"
	elif oldDirection == "R":
		if move == "L":
			result = "U"
		elif move == "R":
			result = "D"
	return result


inputString = "R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3"

splitInput = re.split(', ', inputString)
currentDirection = "U" #Initially facing upwards
currentLocation = [0,0] #[x,y] coordinates of where you currently are

#A list of lists containing the coordinates of all locations that have been visited
visitedLocations = [[0,0]]

#Loop through splitInput
for i in splitInput:
	#This is the direction that you have moved and are now currently facing
	currentDirection = newDirection(currentDirection, i[0])

	#The number following the 'L'/'R' 
	distance = int(i[1:])

	#Update visitedLocations
	for j in range(distance):

		newLocation = currentLocation[:]

		if currentDirection == "U":
			newLocation[1] += j + 1
		elif currentDirection == "D":
			newLocation[1] -= j + 1
		elif currentDirection == "L":
			newLocation[0] -= j + 1
		elif currentDirection == "R":
			newLocation[0] += j + 1

		#Check if newLocation is in visitedLocations. If it is, that is the HQ location (therefore, exit).
		#If not, append it to visitedLocations.

		for k in visitedLocations:
			if (newLocation == k):
				print("HQ is at: " + str(newLocation))
				distanceHQ = abs(newLocation[0]) + abs(newLocation[1])
				print("Distance from HQ: " + str(distanceHQ))
				exit() 
		visitedLocations.append(newLocation)

	#Update currentLocation
	if currentDirection == "U":
		currentLocation[1] += distance
	elif currentDirection == "D":
		currentLocation[1] -= distance
	elif currentDirection == "L":
		currentLocation[0] -= distance
	elif currentDirection == "R":
		currentLocation[0] += distance