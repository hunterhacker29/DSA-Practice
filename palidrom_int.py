n= 5665
arr= []
isPal= True
for i in str(n):
    arr.append(int(i))
    
left = 0
right = len(arr)-1

while left<right :
    if arr[left]==arr[right]:
        left +=1
        right -=1
    else :
        ispal=False
        break

print(isPal)
    