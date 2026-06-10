def sortElements(array,low,high):
    pivote = array[low]
    i=low
    j=high
    while (i < j):
        while(i < high and array[i] <= pivote  ):
            i += 1
        while( j > low and array[j] >= pivote):
            j -= 1
        if (i < j):
            array[j],array[i] = array[i],array[j]

    array[low],array[j] = array[j],array[low]
    return j
        
def quicksort(array,low,high):
    if (low >= high):
        return array

    pivotePossition = sortElements(array,low,high)
    quicksort(array,low,pivotePossition-1)
    quicksort(array,pivotePossition+1,high)
    return array
    
array=[2,3,5,6,1,2,3,8,34,5,6]
print(quicksort(array,0,len(array)-1))