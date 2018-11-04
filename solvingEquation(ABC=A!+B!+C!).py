"""
Solution for problem in the video:)

https://www.youtube.com/watch?v=gAPNzzeNWZg


ABC=A!+B!+C!




I LOVE PYTHON
"""
from math import factorial as fact
for x in range(1,10):
	for y in range(0,10):
		for z in range(0,10):
			nmbr=str(x)+str(y)+str(z)
			if int(nmbr)==fact(x)+fact(y)+fact(z):
				print ("congratulations! You succesfuly find the answer which is:"+str(nmbr))
			else:
				continue
