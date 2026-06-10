def sortElements(n):
    for i in range(len(n)):
        min = i
        for j in range(i,len(n)):
            if n[j] < n[min]:
                min = j
        n[i],n[min]=n[min],n[i]

    return n
# print(sortElements([4,6,1,3,8,9,3]))
def largest(n):
    if len(n) < 2:
        secondsmallest = -1
        secondLarge = -1
    else:
        sortedArray = sortElements(n)
        print(sortedArray)
        largest = sortedArray[-1]
        smallest = sortedArray[0]
        secondLarge = 0
        secondsmallest = sortedArray[-1] +1

        for i in range(len(n)):
            if sortedArray[i] > smallest and sortedArray[i] != largest:
                secondLarge = sortedArray[i]
            elif sortedArray[i] == smallest:
                secondLarge = sortedArray[i]
        for j in range(len(n)-1,-1,-1):
            if sortedArray[j] < largest and sortedArray[j] != smallest:
                secondsmallest = sortedArray[j]
            elif sortedArray[j] == largest:
                secondsmallest = sortedArray[j]
    print("smallest :",secondsmallest,"largest :",secondLarge)   
largest([3,5,2,7,3,6,1,9])