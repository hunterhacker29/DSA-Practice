nn = 153 
arr=[]

for i in str(nn):
    arr.append(int(i))

print(arr)

n = len(arr)
count = 0
for i in range(n):
    arr[i]=arr[i] ** n
    count +=arr[i] 

print(arr)
print(count)

if nn==count:
    print("Armstrong")
else :
    print(False)