

def binarySearch(arr,target):
    
    left = 0 
    right = len(arr)-1 
    
    mid = 0 
    i=0
    while left <= right :
        
        mid = (left+right)//2 
        
        if arr[mid] ==  target:
            return f'Element {target} Found At index {mid} '

        elif target < mid :
            right=mid-1 
        
        else :
            left= mid+1
                



if __name__ == '__main__':

    arr = [10,20,30,40,50]
    
    print(binarySearch(arr,30))
    
    
    