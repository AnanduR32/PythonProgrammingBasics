def bubbleSort(nList):
    for i in range(0,len(nList)-1):
        for j in range(0,len(nList)-i-1):
            if(nList[j]>nList[j+1]):
                nList[j], nList[j+1] = nList[j+1],nList[j]

nList = [int(x) for x in input('Enter the array of elements to be sorted: ').split()]
bubbleSort(nList)
print('The sorted array: '+str(nList))