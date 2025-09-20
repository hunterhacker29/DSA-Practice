def dublicate(arr):
    
    n = len(arr)
    
    for i in range(n):
        for j in range (i+1,n):
            if arr[i] == arr[j]:
                return True

arr = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(dublicate(arr))  