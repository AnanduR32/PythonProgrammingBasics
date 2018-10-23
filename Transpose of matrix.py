import numpy as np
b=[[0,0,0],[0,0,0],[0,0,0]]
a=np.arange(9).reshape(3,3)
print("\n")
for i in range(0,3):
    print()
    for j in range(0,3):
        print(a[i][j],end='')
        if(j>2):
            break
print("\n")
print("The transpose of the matrix is :\n")
for i in range(0,3):
    for j in range(0,3):
        b[j][i]=a[i][j]
for i in range(0,3):
    print()
    for j in range(0,3):
        print(b[i][j],end='')
        if(j==3):
            break


