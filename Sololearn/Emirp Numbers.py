"""
Emirp Numbers

An emirp is a prime number that results in a different prime when its decimal digits are reversed. For example, 13 is an emirp number because both 13 and 31 are prime numbers.

For example:
Input: 17
Output: true (17 and 71 are prime numbers)

Input: 113
Output: true (113 and 311 are prime numbers)

Input: 23
Output: false (23 is a prime number, but 32 is not)

Write a program to check if the user input is an emirp number or not.
"""
def checkPrime(x):
	if x==2:
		return True
	for y in range(2,x):
		if x%y==0:
			return False
		else:
			return True
def checkEmirp(num):
	if checkPrime(num) and checkPrime(int(str(num)[::-1])):
		print "{} is an emirp number".format(num)
	else:
		print "{} isn't an emirp number".format(num)
checkEmirp(113)