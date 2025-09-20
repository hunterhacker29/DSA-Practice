def reverse(arr):
    
    n = len(arr)
    left =0
    right = n - 1
     
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        
    return arr


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr)
print(reverse(arr)) 
        