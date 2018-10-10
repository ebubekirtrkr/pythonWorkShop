import os
# for fname in os.listdir("."):
# 	if fname.endswith(".py"):
# 		continue
# 	else:
# 		if fname[-8]=="_":
# 			if fname[-6]=="_":
# 				spltName=fname.split("_")
# 				newName=spltName[0]+"_0"+spltName[1]
# 				os.rename(fname,newName)
# 				print str(fname)+" renamed"
#			elif fname[-7]=="_":
# 				spltName=fname.split("_")
# 				newName=spltName[0]+"_00"+spltName[1]
# 				os.rename(fname,newName)
# 				print str(fname)+" renamed"
# 		elif fname[-6]=="_":
# 			spltName=fname.split("_")
# 			newName=spltName[0]+"_0"+spltName[1]
# 			os.rename(fname,newName)
# 			print str(fname)+" renamed"



# os.system("copy NUL 77_4.txt && copy NUL 77_3.txt")
# filename, file_extension = os.path.splitext('/path/to/somefile.ext')
# print filename, file_extension	
# arr=[1,2,10]
# for bas in range(10):
# 	for son in arr:
# 		cmnd="copy NUL "+str(bas)+"_"+str(son)+".txt"
# 		os.system(cmnd)

# arr=[1,2,10,100,101,99,200,102]
# for bas in range(10):
# 	for son in arr:
# 		cmnd="copy NUL "+str(bas)+"_"+str(son)+".txt"
# 		os.system(cmnd)

arr=[1,2,3,4,5]
for x in arr:
	cmnd1="mkdir "+str(x)
	os.system(cmnd1)
	for end in range(1,103):
		fileName=str(x)+"_"+str(end)+".txt"
		cmnd="copy NUL "+fileName
		os.system(cmnd)
		cmnd2="move "+fileName+" .\\"+str(x)
		os.system(cmnd2)
			