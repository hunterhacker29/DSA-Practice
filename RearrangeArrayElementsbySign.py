a= [1,2,-4,-5,6,-7]
p=[]
n=[]

for i in range(len(a)) :
    if a[i]<0:
        n.append(a[i])
    else :
        p.append(a[i])
        


print(a)
print(p)
print(n)
        
        
for i in range(len(p)):
    a[2*i]=p[i]
    a[(2*i)+1]=n[i]
    
    

print(a)