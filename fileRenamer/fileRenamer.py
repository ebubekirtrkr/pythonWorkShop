import os
for sure in range(1,115):
	path="./"+str(sure)
	for fname in os.listdir(path):
		if fname.endswith(".py"):
			continue
		elif len(os.listdir(path))>99:
			splitUnder=fname.split("_")#1,100.txt
			splitPeriod=splitUnder[1].split(".")#100, txt
			if int(splitPeriod[0])<10:
				newName=splitUnder[0]+"_00"+splitUnder[1]
				pathfname=path+"/"+fname
				pathnewName=path+"/"+newName
				os.rename(pathfname,pathnewName)
				print str(fname)+" is renamed"
			elif int(splitPeriod[0])<100:
				newName=splitUnder[0]+"_0"+splitUnder[1]
				pathfname=path+"/"+fname
				pathnewName=path+"/"+newName
				os.rename(pathfname,pathnewName)
				print str(fname)+" is renamed"
			elif int(splitPeriod[0])<999:
				continue
		else:
			splitUnder=fname.split("_")#1,99.txt
			splitPeriod=splitUnder[1].split(".")#99, txt
			if int(splitPeriod[0])<10:
				newName=splitUnder[0]+"_0"+splitUnder[1]
				pathfname=path+"/"+fname
				pathnewName=path+"/"+newName
				os.rename(pathfname,pathnewName)
				print str(fname)+" is renamed"
