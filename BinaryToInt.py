bn = "1101"
dec= 0

arr= [int(i) for i in bn]
arr=arr[::-1]
for i in range(len(arr)) :
    dec += arr[i]*2**i

    

print(dec)
    