ma=[[2,3,4],[6,7,1]]
mb=[[65,32,12],[87,66,10]]
mc=[[0,0,0],[0,0,0]]
for i in range(0,2):
    for j in range(0,3):
        mc[i][j]=ma[i][j]+mb[i][j]
print(mc)

