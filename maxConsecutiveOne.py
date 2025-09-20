arr= [1,1,0,1,0,1,1,1,1,0,1,1,1,1,1]
ans = 0
mx= 0
for i in range(len(arr)-1):
    if arr[i]==arr[i+1]:
        mx +=1
        ans = max (mx,ans)
    else :
        mx=0


print(arr)
print(ans+1)