
# bruet force approach


arr = [1,3,-1,2,-1,4]
n = len(arr)
k = 3 



list = []

for i in range(n-k+1):
    maxx= arr[i]
    
    for j in range(i,i+k):
        maxx= max(maxx,arr[j])
    
    list.append(maxx)
    
    
print(list)
sum = 0
for i in list:
    sum = sum + i 
    


print(sum)