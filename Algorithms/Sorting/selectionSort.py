def selectionSort(nList):
    for i in range(0,len(nList)):
        min_idx = i
        for j in range(i,len(nList)):
            if(nList[j]<nList[min_idx]): # Interchange b/n < and > to get ascending..
                min_idx = j              # or descending sort respectively
        nList[i], nList[min_idx] = nList[min_idx],nList[i]

nList = [int(x) for x in input('Enter the array of elements to be sorted: ').split()]
selectionSort(nList)
print('The sorted array: '+str(nList))