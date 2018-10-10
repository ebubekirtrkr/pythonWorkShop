main_arr=[10,20,30,40,50,60]
output_arr=[]
for x in main_arr:
    for y in main_arr:
        for z in main_arr:
            if x==y or y==z or x==z:
                continue
            else:
                if (abs(x-y)<z and abs(x+y)>z) and (abs(x-z)<y and abs(x+z)>y) and (abs(z-y)<x and abs(z+y)>x) :
                    sorted_arr=sorted([x,y,z])
                    if sorted_arr not in output_arr:
                        output_arr.append(sorted_arr)
print (output_arr)
print ("\n")
print (len(output_arr))