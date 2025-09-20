# bruetforce approach


arr = [19,4,2,11,6,5,3,10]
ans = 0
maxx = 0
result = []

for i in range(len(arr)):
    ans = -1 
    maxx = arr[i]
    
    for j in range(i+1,len(arr)):
        if arr[j] > maxx:
            maxx = arr[j]
            ans = max(maxx, ans)   # <-- confusing part
    
    result.append(ans)

print(arr)
print(result)   # <-- only prints last one!
