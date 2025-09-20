def movZero(arr):
    
    pos = 0 
    
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[pos]=arr[i]
            pos+=1 
            
            
    print(pos)     
    while pos < len(arr):
        arr[pos] =0
        pos +=1 
    
    

arr= [0,1,0,3,12]
print(arr)
movZero(arr)
print(arr)
