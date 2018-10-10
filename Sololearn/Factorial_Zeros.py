from math import factorial 
nmbr=int(input("Please Enter Number\n"))
fact=factorial(nmbr)
res=0
while str(fact).endswith(str(0)):
	res +=1
	fact/=10
print "result:{}".format(res)