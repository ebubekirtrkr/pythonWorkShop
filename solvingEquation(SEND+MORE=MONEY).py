"""
Solution for problem in the video:)

https://www.youtube.com/watch?v=ZXO3jwV0nl0



SEND + MORE = MONEY , M!=0


s,e,n,d,m=1,o=0,r,y

 		SEND 
 		MORE
____________
	   MONEY



I LOVE PYTHON
"""

for s in range(2,10):
	for e in range(2,10):
		for n in range(2,10):
			for d in range(2,10):
				for r in range(2,10):
					for y in range(2,10):
						arr=[s,e,n,d,r,y]
						un_ar=[]
						for i in arr:
							if i not in un_ar:
								un_ar.append(i)
						ilk=int(str(s)+str(e)+str(n)+str(d))
						iki=int(str(1)+str(0)+str(r)+str(e))
						son=int(str(1)+str(0)+str(n)+str(e)+str(y))
						if ilk+iki==son and len(un_ar)==6:
							print ilk,iki,son
							print un_ar
						else:
							continue