#!/usr/bin/python

inputText = []
inputText.append("LURLLLLLDUULRDDDRLRDDDUDDUULLRLULRURLRRDULUUURDUURLRDRRURUURUDDRDLRRLDDDDLLDURLDUUUDRDDDLULLDDLRLRRRLDLDDDDDLUUUDLUULRDUDLDRRRUDUDDRULURULDRUDLDUUUDLUDURUURRUUDRLDURRULURRURUUDDLRLDDDDRDRLDDLURLRDDLUDRLLRURRURRRURURRLLRLDRDLULLUDLUDRURDLRDUUDDUUDRLUDDLRLUDLLURDRUDDLRURDULLLUDDURULDRLUDLUDLULRRUUDDLDRLLUULDDURLURRRRUUDRUDLLDRUDLRRDUDUUURRULLDLDDRLUURLDUDDRLDRLDULDDURDLUUDRRLDRLLLRRRDLLLLURDLLLUDRUULUULLRLRDLULRLURLURRRDRLLDLDRLLRLULRDDDLUDDLLLRRLLLUURLDRULLDURDLULUDLRLDLUDURLLLURUUUDRRRULRDURLLURRLDLRLDLDRRUUDRDDDDDRDUUDULUL")
inputText.append("RRURLURRULLUDUULUUURURULLDLRLRRULRUDUDDLLLRRRRLRUDUUUUDULUDRULDDUDLURLRRLLDLURLRDLDUULRDLLLDLLULLURLLURURULUDLDUDLUULDDLDRLRRUURRRLLRRLRULRRLDLDLRDULDLLDRRULRDRDUDUUUDUUDDRUUUDDLRDULLULDULUUUDDUULRLDLRLUUUUURDLULDLUUUULLLLRRRLDLLDLUDDULRULLRDURDRDRRRDDDLRDDULDLURLDLUDRRLDDDLULLRULDRULRURDURRUDUUULDRLRRUDDLULDLUULULRDRDULLLDULULDUDLDRLLLRLRURUDLUDDDURDUDDDULDRLUDRDRDRLRDDDDRLDRULLURUDRLLUDRLDDDLRLRDLDDUULRUDRLUULRULRLDLRLLULLUDULRLDRURDD")
inputText.append("UUUUUURRDLLRUDUDURLRDDDURRRRULRLRUURLLLUULRUDLLRUUDURURUDRDLDLDRDUDUDRLUUDUUUDDURRRDRUDDUURDLRDRLDRRULULLLUDRDLLUULURULRULDRDRRLURULLDURUURDDRDLLDDDDULDULUULLRULRLDURLDDLULRLRRRLLURRLDLLULLDULRULLDLRULDDLUDDDLDDURUUUURDLLRURDURDUUDRULDUULLUUULLULLURLRDRLLRULLLLRRRRULDRULLUURLDRLRRDLDDRLRDURDRRDDDRRUDRLUULLLULRDDLDRRLRUDLRRLDULULRRDDURULLRULDUDRLRUUUULURLRLRDDDUUDDULLULLDDUDRLRDDRDRLDUURLRUULUULDUDDURDDLLLURUULLRDLRRDRDDDUDDRDLRRDDUURDUULUDDDDUUDDLULLDRDDLULLUDLDDURRULDUDRRUURRDLRLLDDRRLUUUDDUUDUDDDDDDDLULURRUULURLLUURUDUDDULURDDLRDDRRULLLDRRDLURURLRRRDDLDUUDR")
inputText.append("URLLRULULULULDUULDLLRDUDDRRLRLLLULUDDUDLLLRURLLLLURRLRRDLULRUDDRLRRLLRDLRRULDLULRRRRUUDDRURLRUUDLRRULDDDLRULDURLDURLRLDDULURDDDDULDRLLUDRULRDDLUUUDUDUDDRRUDUURUURLUUULRLULUURURRLRUUULDDLURULRRRRDULUDLDRLLUURRRLLURDLDLLDUDRDRLLUDLDDLRLDLRUDUULDRRLLULDRRULLULURRLDLUUDLUDDRLURDDUDRDUDDDULLDRUDLRDLRDURUULRRDRUUULRUURDURLDUDRDLLRUULUULRDDUDLRDUUUUULDDDDDRRULRURLLRLLUUDLUDDUULDRULDLDUURUDUDLRULULUULLLLRLULUDDDRRLLDRUUDRLDDDRDDURRDDDULURDLDLUDDUULUUURDULDLLULRRUURDDUDRUULDLRLURUDLRDLLLDRLDUURUDUDRLLLDDDULLUDUUULLUUUDLRRRURRRRRDUULLUURRDUU")
inputText.append("UDULUUDLDURRUDDUDRDDRRUULRRULULURRDDRUULDRLDUDDRRRRDLRURLLLRLRRLLLULDURRDLLDUDDULDLURLURUURLLLDUURRUUDLLLUDRUDLDDRLRRDLRLDDDULLRUURUUUDRRDLLLRRULDRURLRDLLUDRLLULRDLDDLLRRUDURULRLRLDRUDDLUUDRLDDRUDULLLURLRDLRUUDRRUUDUDRDDRDRDDLRULULURLRULDRURLURLRDRDUUDUDUULDDRLUUURULRDUDRUDRULUDDULLRDDRRUULRLDDLUUUUDUDLLLDULRRLRDDDLULRDUDRLDLURRUUDULUDRURUDDLUUUDDRLRLRLURDLDDRLRURRLLLRDRLRUUDRRRLUDLDLDDDLDULDRLURDURULURUDDDUDUULRLLDRLDDDDRULRDRLUUURD")

#Initialise a 2D list containing the keypad:
#  1  
# 234  
#56789
# ABC 
#  D 
keypad = [];
for i in range(5):
	keypad.append([])
	for j in range(5):
		keypad[i].append("")
keypad[0][0] = ""
keypad[0][1] = ""
keypad[0][2] = "5"
keypad[0][3] = ""
keypad[0][4] = ""
keypad[1][0] = ""
keypad[1][1] = "2"
keypad[1][2] = "6"
keypad[1][3] = "A"
keypad[1][4] = ""
keypad[2][0] = "1"
keypad[2][1] = "3"
keypad[2][2] = "7"
keypad[2][3] = "B"
keypad[2][4] = "D"
keypad[3][0] = ""
keypad[3][1] = "4"
keypad[3][2] = "8"
keypad[3][3] = "C"
keypad[3][4] = ""
keypad[4][0] = ""
keypad[4][1] = ""
keypad[4][2] = "9"
keypad[4][3] = ""
keypad[4][4] = ""

code = []

invalidUp = ['1','2','5','4','9'] #numbers for which an 'up' move is invalid
invalidDown = ['5','9','A','C','D'] #numbers for which a 'down' move is invalid
invalidLeft = ['1','2','5','A','D'] #numbers for which a 'left' move is invalid
invalidRight = ['1','4','9','C','D'] #numbers for which a 'right' move is invalid

for line in inputText:
	currentIndex = [2,0] #the 2D list index location of 5, which is the starting point
	for move in line:
		if move == 'U' and keypad[currentIndex[0]][currentIndex[1]] not in invalidUp:
			currentIndex[1] -= 1
		elif move == 'D' and keypad[currentIndex[0]][currentIndex[1]] not in invalidDown:
			currentIndex[1] += 1
		elif move == 'L' and keypad[currentIndex[0]][currentIndex[1]] not in invalidLeft:
			currentIndex[0] -= 1
		elif move == 'R' and keypad[currentIndex[0]][currentIndex[1]] not in invalidRight:
			currentIndex[0] += 1
	code.append(keypad[currentIndex[0]][currentIndex[1]]) 

print("The code is " + str(code))