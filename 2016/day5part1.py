#!/usr/bin/python3

import md5

input = "ffykfhsq"
password = [] #a list containing the characters of the password
numFound = 0 #number of password characters found so far
i = 0

while True:
	string = input + str(i)
	hash = md5.new(string).hexdigest()
	if hash[0:5] == "00000":
		password.append(hash[5])
		numFound += 1
	if numFound == 8: #if all 8 characters of the password are found, break
		break
	i += 1

print("The password is " + ''.join(password))