arr = [1, 2, 2, 3, 1, 4, 2]  # input array


max_val = max(arr)
hash_array = [0] * (max_val + 1)



for num in arr:
    hash_array[num] += 1

'''
        OR 
        
for i in range(len(arr)):
    hash_array[arr[i]] += 1
    
    
'''
print(arr)

print(hash_array)

for i in range(1, len(hash_array)):
   
        print(f"Element {i} occurs {hash_array[i]} times.")