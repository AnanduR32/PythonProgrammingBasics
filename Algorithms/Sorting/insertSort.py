def insertSort(nList):
    for i in range(1,len(nList)):
        key = nList[i]
        j = i - 1
        while(j>=0 and nList[j]>key): # interchange between List[j]>key and List[j]<key.. 
            nList[j+1] = nList[j]     # to sort in ascending or descending order respectively
            j-=1
        nList[j+1] = key

nList = [int(x) for x in input('Enter the array of elements to be sorted: ').split()]
insertSort(nList)
print('The sorted array: '+str(nList))