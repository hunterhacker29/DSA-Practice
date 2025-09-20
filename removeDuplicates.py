def removeDuplicate(arr):
    arr.sort()
    narr = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:  
            narr.append(arr[i])
    
    print(narr)
    print(f'The original size of array is {len(narr)}')


if __name__ == '__main__':
    arr = [1, 1, 2, 2, 3, 5, 6, 5, 6]
    print(arr)
    removeDuplicate(arr)
