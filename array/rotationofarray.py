array = [1,2]
def reverse(arr, low, high):
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
def right_rotate(array,k):
    k= k% len(array)
    reverse(array,0,len(array)-1)
    reverse(array,0,k-1)
    reverse(array,k,len(array)-1)
    return array
print(right_rotate([1,2,3,4,5,6],4))

def left_rotation(array,k):
    k = k%len(array)

    reverse(array,0,k-1)
    reverse(array,k,len(array)-1)
    reverse(array,0,len(array)-1)
    return array
print(left_rotation([1,2,3,4,5,6],4))


# ------------tried oone-------------------
def rot(array,k):
    k = k%len(array)
    n=len(array)

    reverse(array,n-k,n-1)
    reverse(array,0,(n-k)-1)
    reverse(array,0,n-1)
    return array
print(rot([1,2],4))