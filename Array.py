# if __name__ == '__main__':
    
#     arr= [1,2,3,4]
    
#     print(arr)
#     print(arr[1])
    
    
#     arr.append(5)
#     print(arr)
    
    
#     arr.insert(2,10)
#     print(arr)
    
    
#     arr.remove(5)
#     print(arr)
    
#     a= arr[1:3]
#     print(a)  


arr= [2200,2350,2600,2130,2190]

print(arr)

print(f"In Feb month You spend {arr[2]-arr[1]} more than Jan month")
print(f"In first quarter you spent {arr[0]+arr[1]+arr[2]} in total")


n = 2000

for i in arr :
    if i == n :
        print(f"Your spending in month {arr.index(i)+1} is equal to {n}")
        break
    
    else :
        print(f"Your spending in month {arr.index(i)+1} is not equal to {n}")


arr.insert(5, 1980)
print(arr)

a= 200
a= arr[3] - a
print(a)
arr.insert(3,a)
print(arr)