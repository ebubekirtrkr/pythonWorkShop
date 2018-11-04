"""
You have 6 sticks of lengths 10, 20, 30, 40, 50, and 60 centimeters. Find the  number of non-congruent
triangles that can be formed by using three of these sticks as sides 
"""
# The length of any side of a triangle must be larger 
# than the positive difference of the 
# other two sides, but smaller than the sum of 
# the other two sides.


"""
idizi1=[10,20,30,40,50,60]
dizi2=[10,20,30,40,50,60]
dizi3=[10,20,30,40,50,60]
a=0
b=1
c=2
for i in range(6):

    x=dizi1[a]
    y=dizi2[b]
    z=dizi3[c]
    if b==6:
        a+=1
        b=0
    if c==6:
        b+=1
        c=0
        print (x,y,z)
"""