def solve(index, subset):
    if index >= len(nums):
        result.append(subset.copy())
        return 
    
    subset.append(nums[index])
    solve(index+1, subset)   # ⚠️ this line has a problem
    subset.pop()
    solve(index+1, subset)


nums = [5, 9, 7]
result = []
solve(0, [])
print(result)
