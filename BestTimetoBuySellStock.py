def buySell(arr):
    
    max = 0 
    ptr = float('inf')
    

    
    for i in range (len(arr)):
        if arr[i] < ptr:
            ptr = arr[i]
            buyAt=ptr 
            
        elif arr[i] - ptr > max :
            max = arr[i] - ptr
            sell= arr[i]
            
    
   
    print(f'Buy Stock at {buyAt}')
    print(f'sell Stock at {sell}')
    print(f'Max profit is {max}')
    

arr= [7,1,5,3,6,8,9,4]
print(arr)
buySell(arr)