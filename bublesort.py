

def Bublesort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
            

if __name__=='__main__':
    
    
    arr= [4,8,2,3,10,20,9]
    
    print(arr)
    
    
    Bublesort(arr)
    print(arr)