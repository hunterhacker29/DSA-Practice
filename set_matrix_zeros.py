def markinfinity(mat,row,col):
    
    r = len(mat)
    c = len(mat[0])
    for i in range(r):
        if mat[i][col]!=0:
            mat[i][col]=float("inf")
    
    for j in range(c):
        if mat[row][j]!=0:
            mat[row][j]=float("inf")
 



mat = [[7,9,5,3],[10,20,0,1],[29,0,8,5],[4,14,6,7]]
print(mat)
rows = len(mat)
columns = len(mat[0])


for i in range(rows):
    for j in range(columns):
        if mat[i][j]==0:
            markinfinity(mat,i,j)
 

for i in range(rows):
    for j in range(columns):
        if mat[i][j]==float('inf'):
            mat[i][j]=0


print(mat)
