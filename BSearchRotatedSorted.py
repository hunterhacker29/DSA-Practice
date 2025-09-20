def BsearchOnrotatedArray(arr,target):
    left, right = 0, len(arr) - 1
    
    while(left<=right):
        
        
        mid = (left + right) // 2
        
        if arr[mid]==target:
            return mid 
        
        elif arr[left] < arr[mid]:
            if arr[left]<=target<=arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else :
            if arr[mid]<=target<=arr[right]:
                left = mid + 1
            else:
                right = mid - 1
            
            






arr = [3,4,5,6,7,0,1,2]
target = 0
print(BsearchOnrotatedArray(arr,0))

