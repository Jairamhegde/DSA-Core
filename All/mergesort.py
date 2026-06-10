
def merge(array,low,mid,midplus,high):
    temp = []
    left=low
    right = midplus
    while( left <= mid and right <= high):
        if array[left] <= array[right]:
                temp.append(array[left])
                left += 1
        else:
            temp.append(array[right])
            right += 1
    while(left <= mid ):
        temp.append(array[left])
        left += 1
    while(right <= high ):
        temp.append(array[right])
        right += 1
    for i in range(low,high+1): 
        array[i] = temp[i-low] 
    return array
''' here array[i] = temp[i-low] because if we are merging specific part of the array say index3 to 6
than, arrays starting index will be 3 and temp arrays starting index will be zero so if you use 
array[i] = temp[i], than it becomes out or range i.e arry[3] = temp[3], but it needs to be array[3] = temp[0]
because low=3 '''
def mergeSort(array,low,high):
    if (low >= high):
        return
    mid = (low + high) // 2
    mergeSort(array,low,mid)
    mergeSort(array,mid+1,high)
    array = merge(array,low,mid,mid+1,high)
    return array
ary = [2,3,1,7,5,4,8,7,1,4,9,3]
print(mergeSort(ary,0,len(ary)-1))

