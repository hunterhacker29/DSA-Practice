

nums =[3,4,4,4,8,9,9,10,12,12,14,15]

target = 11

maxmin= float('inf')
floor = 0 

for i in nums :
    if i >= target:
        maxmin=min(i,maxmin)
    elif i <= target:
        floor=i 
        

print(maxmin)
print(floor)
     
        
