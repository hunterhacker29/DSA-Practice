def m(arr):
    
    
    maximum = 0

    
    for i in range(len(arr)):
        if arr[i]>maximum:
            maximum = arr[i]    
            
    return maximum


def mn (arr):
    min = float('inf')
    n = len(arr)
    
    for i in range (n):
        if arr[i] < min:
            min = arr[i]
        
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(m(arr))
print(mn(arr))

