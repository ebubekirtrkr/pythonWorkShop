"""https://www.codewars.com/kata/iq-test/train/python"""
#def iq_test(numbers):
numbers="1 2 2"
a=numbers.split(" ")
c=""
if int(a[0])%2==1:
    c+="1" 
else:
    c+="0"
if int(a[1])%2==1:
    c+="1" 
else:
    c+="0"
if int(a[2])%2==1:
    c+="1" 
else:
    c+="0"
print(c)
if(c=="001" or c=="000"):
    d=0
    for i in a:
        d+=1
        if(int(i)%2==1):
            break
    print (d)
elif(c=="111" or c=="110"):
    d=0
    for i in a:
        d+=1
        if(int(i)%2==0):
            
            break
    print (d)
elif(c=="011"):
    print (1)
elif(c=="100"):
    print (1)
elif(c=="101"):
    print (2)
elif(c=="010"):
    print (2)
