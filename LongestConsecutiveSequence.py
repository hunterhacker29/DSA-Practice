nums = [1,99,101,98,2,5,3,100,1,102,103]


maxc = 0
count = 0

for i in range(len(nums)):
  num = nums[i]
  count = 1 
  
  while num+1 in nums:
      count+=1
      num = num+1
      maxc = max(maxc,count)
print(maxc)
