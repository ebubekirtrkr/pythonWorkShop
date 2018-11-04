"""
Disarium Numbers

A number is called a Disarium number if the sum of the powers of its digits equals the number itself. The digits are powered to their positions in the number.

For example:
Input: 135
Output: true
135 is a Disarium number because it equals to 1^1 + 3^2 + 5^3 (each digit powered to the position in the number).

Write a program to check if the user input is a Disarium number or not.
"""
nmbr=int(input())
def dissarium(x):
	x=str(x)
	res=0
	pos=1
	for i in x:
		res+=int(i)**pos
		pos+=1
	if res==int(x):
		return True
	else:
		return False
if dissarium(nmbr):
	print "{} is a Disarium number".format(nmbr)
else:
	print "{} isn't a Disarium number".format(nmbr)
