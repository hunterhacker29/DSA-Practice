def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def right_rotate(arr, k):
    n = len(arr)
    k %= n
    print(k)
    
    # Step 1: Reverse the whole array
    reverse(arr, 0, n - 1)
    print(arr)
    # # Step 2: Reverse first k elements
    reverse(arr, 0, k - 1)
    print(arr)
    
    # # Step 3: Reverse the rest
    reverse(arr, k, n - 1)
    print(arr)
    

# Example
arr = [1, 2, 3, 4, 5]
right_rotate(arr, 2)
print("Rotated Array:", arr)
