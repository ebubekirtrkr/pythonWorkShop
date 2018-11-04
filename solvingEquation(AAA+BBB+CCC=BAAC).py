"""
Solution for problem in the video:)

https://www.youtube.com/watch?v=ZXO3jwV0nl0



AAA + BBB + CCC = BAAC



I LOVE PYTHON
"""
for x in range(1,10):
	for y in range(0,10):
		for z in range(0,10):
			A=str(x)*3
			B=str(y)*3
			C=str(z)*3
			temp =int(str(y)+str(x)+str(x)+str(z))
			res=int(A)+int(B)+int(C)
			if res==temp:
				print("AAA + BBB + CCC = BAAC")
				print (A+" + "+B+" + "+C+" = "+str(res))
				print ("A"+"="+str(x)+"\tB"+"="+str(y)+"\tC"+"="+str(z))
			else:
				continue