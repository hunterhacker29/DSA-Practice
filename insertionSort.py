
def InsersionSort(arr):
    
    n= len(arr)
    
    for i in range(1,n):
        temp = arr[i]
        j= i-1 
        while (j>= 0 and arr[j]>temp):
            
            arr[j+1] = arr[j]
            j = j-1 
        
        arr[j+1] = temp

if __name__== "__main__":
    
    arr= [3,4,5,6,8,9,10,7,1]
    print(arr)
    InsersionSort(arr)
    print(arr)