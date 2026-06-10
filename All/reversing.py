array=[3,4,6,7,1,2]
i=0
j=len(array)-1

newarr=[]
while(i<j):
    array[i],array[j]=array[j],array[i]
    j-=1
    i+=1
print(array)