from itertools import product

alpha = [
    [], [], ["a","b","c"], ["d","e","f"], ["g","h","i"], ["j","k","l"],
    ["m","n","o"], ["p","q","r","s"], ["t","u","v"], ["w","x","y","z"]
]

digit = 46

# Step 1: convert number into a list of digits
num = []
for i in str(digit):      # "46" → "4" then "6"
    num.append(int(i))    # → [4, 6]

print("Digits:", num)

# Step 2: get all letter lists for these digits
letters = []
for i in num:             # [4, 6]
    letters.append(alpha[i])

print("Letters:", letters)


comb= []
for i in product(*letters):
    word =""
    for j in i :
        word= word+j
    
    print(word)
    comb.append(word)
 
print(comb)
    