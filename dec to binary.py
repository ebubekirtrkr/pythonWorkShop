def dectobin(y):
	if y==0:
		return "0"
	if y==1:
		return "1"
	h=""
	while y>1:
		x=int(y/2)
		rmdnr=y%2#remainder
		y=int(y/2)
		h+=str(rmdnr)
		if x>1:
			continue
		else:
			h+=str(x)
	h=h[::-1]
	return h
for i in range(0,10):
	print (str(i)+"   =   "+dectobin(i))
