m,n,r=[int(x) for x in input().split()]
matrix1=[]
for i in range(m):
        row=[int(x) for x in input().split(' ',n)]
        matrix1.append(row)
def rotate(mat):
  res1=[]
  for i in range(m):
    row=[int(0) for x in range(n)]
    res1.append(row)
  matrix1=mat
  row1=m-1 
  column1=n-1 
  j1=0
  def fun(matrix,res,j,row,column):
    for i in range(j,row):
       res[i+1][j]=matrix[i][j]
       res[i][column]=matrix[i+1][column]
    for i in range(j,column):
       res[j][i]=matrix[j][i+1]
       res[row][i+1]=matrix[row][i]
    return res
  res=fun(matrix1,res1,j1,row1,column1)
  if m-2>0 and n-2>0:
     if m-2==1 and n-2==1:
        res[1][1]=matrix1[1][1]
     else:
      j1+=1
      row1-=1
      column1-=1
      res=fun(matrix1,res1,j1,row1,column1)
  return res
result=rotate(matrix1)
while r>1:
   r-=1
   result=rotate(result)
for i in range(m):
   for j in range(n):
      print(result[i][j],end=' ')
   print()