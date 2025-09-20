def max_consecutive_ones(nums):
    n = len(nums)
    max_count = 0
    current_count = 0

    for i in range(n):
        if nums[i] == 1:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0  # Reset if not 1

    return max_count

    

arr= [0,1,1,1,0,3,2,1,0,1,1,1,1,1,1]
print(arr)
max_consecutive_ones(arr)
print(max_consecutive_ones(arr))