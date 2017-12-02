#!/usr/bin/python3

import md5

input = "ffykfhsq"
password = ['_'] * 8 #a list containing the characters of the password
found = ['0'] * 8 #list of 8 characters representing the password characters found so far
				#'0' = not found, '1' = found
i = 0

while True:
	string = input + str(i)
	hash = md5.new(string).hexdigest()
	if (hash[0:5] == "00000") and ('0' <= hash[5] and hash[5] <= '7') and (found[int(hash[5])] == '0'):
		password[int(hash[5])] = str(hash[6])
		found[int(hash[5])] = '1'
		print("Characters found so far: " + ''.join(password)) #Prints a cinematic decrypting animation
	if ''.join(found) == '11111111': #if all 8 characters of the password are found, break
		break
	i += 1

print("The password is " + ''.join(password))