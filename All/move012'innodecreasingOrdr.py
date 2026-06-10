def sortOnes(array):

    low,mid,high = 0,0,len(array)-1

    while(mid < high):
        if array[mid] == 0:
            array[low],array[mid]=array[mid],array[low]
            mid += 1
            low += 1
        if array[mid] == 2:
            array[mid],array[high]= array[high],array[mid]
            high -= 1
            mid += 1
        if array[mid] == 1:
            mid += 1
    return array

print(sortOnes([1,1,0,2,0,0,1,2,0]))

def move(n):
    zeros=ones=twos=0

    for a in n:
        if a == 0:
            zeros += 1
        elif a == 1:
            ones += 1
        else:
            twos += 1
    for i in range(zeros):
        n[i] = 0
    for j in range(zeros, ones+zeros):
        n[j] = 1

    for k in range(zeros+ones,len(n)):
        n[k] = 2

    return n
print(move([1,0,2,0,0,1,1,1,0,2,2,0,1]))

