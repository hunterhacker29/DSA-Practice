
# '''
# To solve this, I'm starting with a brute-force 
# approach that checks every pair of elements 
# to see if they sum to the target. It runs
# in O(n²) time, which is acceptable for 
# small inputs. Once this works, 
# I’ll optimize it using a hash map for 
# O(n) time."
# '''



# def TwoSum(arr,target):
    
#     for i in range(len(arr)):
#         for j in range (i+1,len(arr)):
#             if arr[i]+arr[j]==target:
#                 return arr[i] , arr[j]
    




# arr = [2, 7, 11, 15]
# target = 22

# print(arr)
# print(f'the Two sum {TwoSum(arr,target)} is :{target} ')

# using two pointer


def Twosum(arr,target):
    

    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
    start = 0 
    end = len(arr)-1
    
    while start < end:
        new_sum = arr[start]+arr[end]
        
        if new_sum == target:
            return arr[start],arr[end]
        
        elif new_sum<target:
            start +=1
        else:
            end -=1
            
arr= [10,20,17,5]
target = 25

print(Twosum(arr,25))

