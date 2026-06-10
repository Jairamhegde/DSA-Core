def sortedd(ar):
    n=ar
    for i in range(len(n)):
        for j in range(i,len(n)):
            if n[i] > n[j]:
                temp = n[i]
                n[i] = n[j]
                n[j] = temp

    return n
print(sortedd([2,5,79,79,79,6,9,1,1,1,5,70]))
def largest(nn):
    n=sortedd(nn)
    largest=n[-1]
    smallest=n[0]
    secondLargest=-1
    secondsmallest=largest+1
    # print(largest)
    # print(smallest)
    for m in range(0,len(n)):
       if n[m] > secondLargest and n[m] != largest:
           secondLargest = n[m]
    for k in range(len(n)-1,-1,-1):
        if secondsmallest > n[k] and n[k] != smallest:
            secondsmallest = n[k]
    print("second smallest :",secondsmallest)
    print("second largest :",secondLargest)

            
largest([2,5,79,79,79,6,9,1,1,1,5,70])
print(12*10**-6)