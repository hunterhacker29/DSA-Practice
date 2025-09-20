def find (arr):
    
    n = len (arr)
    print(n)
    tot = n * (n+1)//2
    actual_sum = sum(arr)
    
    
    
    print(tot)
    print(actual_sum)
    miss = tot - actual_sum
    print (f'The missing element is {miss}')




arr = [0,1,2,4,5]
print(arr)
find(arr)