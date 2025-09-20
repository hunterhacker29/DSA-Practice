arr = [1, 2, 1, 2, 5, 5, 6, 7, 8]

hmap = {}

for i in arr:
    if i in hmap:
        hmap[i] += 1
    else:
        hmap[i] = 1

print(hmap)



# # or using Array 

arr = [1, 2, 1, 2, 5, 5, 6, 7, 8]

# Find max element to decide array size
max_val = max(arr)

# Make freq array initialized with 0
freq = [0] * (max_val + 1)

# Count frequencies
for i in arr:
    freq[i] += 1

print(freq)
