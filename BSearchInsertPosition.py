def search_insert(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low+high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        print(low)

    
    return low



arr= [1,2,4,5,6,7,15,20,60,70,75,80]
target = 78
print(search_insert(arr, target))  