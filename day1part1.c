#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char newDirection (char oldDirection, char move);

int main (int argc, char *argv[]) {
	int numRight = 0;
	int numLeft = 0;
	int numUp = 0;
	int numDown = 0;
	char *input = "R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3,"; //I added a comma to the end of the input

	char currentDirection = 'U';

	//Loop through the string
	int i = 0;
	for (i = 0; input[i] != '\0'; i++) {
		if (input[i] == 'L' || input[i] == 'R') {
			int numSteps = 0;
			int j;
			for (j = i + 1; input[j] != ','; j++) { //Loop across the numbers following the 'L'/'R' char;
				numSteps = numSteps * 10;
				numSteps += input[j] - '0'; //convert char to int
			}

			currentDirection = newDirection(currentDirection, input[i]);
			if (currentDirection == 'U') numUp += numSteps;
			else if (currentDirection == 'D') numDown += numSteps;
			else if (currentDirection == 'L') numLeft += numSteps;
			else if (currentDirection == 'R') numRight += numSteps;
		}
	}

	//Calculate the final distance
	int finalDistance = abs(numUp-numDown) + abs(numLeft-numRight);
	printf("The final distance is: %d\n", finalDistance);
	return EXIT_SUCCESS;
}

//Takes 2 arguments:
//    oldDirection = direction you are currently facing (U/D/L/R)
//    move = the move you made (L/R)
//Returns the new direction you are facing (U/D/L/R)
char newDirection (char oldDirection, char move) {
	char result = '\0';
	if (oldDirection == 'U') { //facing up
		if (move == 'L') {
			result = 'L';
		} else if (move == 'R') {
			result = 'R';
		}
	} else if (oldDirection == 'D') { //facing down
		if (move == 'L') {
			result = 'R';
		} else if (move == 'R') {
			result = 'L';
		}
	} else if (oldDirection == 'L') { //facing left
		if (move == 'L') {
			result = 'D';
		} else if (move == 'R') {
			result = 'U';
		}
	} else if (oldDirection == 'R') { //facing right
		if (move == 'L') {
			result = 'U';
		} else if (move == 'R') {
			result = 'D';
		}
	}
	return result;
}