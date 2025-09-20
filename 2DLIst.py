arr  = [[10,20,30],[40,50,60],[70,80,90]]

rows = len(arr)
columns = len(arr[0])


print(arr)
print('rows :',rows)
print('columns  :',columns)

for i in range(rows):
    for j in range(columns):
        print(arr[i][j],end = " ")
        
print('\n-----------------------------------------------------------------')


for i in range(rows):
    for j in range(columns):
        if j >=i:
            
            print(arr[i][j],end = " ")
        else :
            print('*',end=' ')


print('\n-----------------------------------------------------------------')

for i in range(rows):
    for j in range(columns):
        if j ==i:
            
            print(arr[i][j],end = " ")
        else :
            print('*',end=' ')
            
