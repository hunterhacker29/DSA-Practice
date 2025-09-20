

def kdane(arr):
    
    max_count = 0 
    current_count = 0 
    
    for i in range(len(arr)):
        if current_count == 0:
            current_count = arr[i]
            
        else :
            current_count = current_count+arr[i]
            
        if current_count > max_count:
            max_count= current_count
            
    
    return max_count


arr =  [-2,1,-3,4,-1,2,1,-5,4]  

print(arr)

print(kdane(arr))