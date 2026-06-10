# def pattern(n):
#     for i in range((n*2)+1):
#         stars=i
#         if i>n:
#             stars=((2*n)-i)
#         for j in range(stars):
#             print("*",end="")
            
#         print()
   
# pattern(2)


# def pattern(n):
#     start=0
#     for i in range(n):
#         if (i % 2 == 0):
#             start=0
#         else:
#             start=1
#         for j in range(i):
#             print(start,end="")
#             if start == 0:
#                 start = 1
#             else:
#                 start = 0
#         print()
        
# pattern(6)

# for i in range(1,4+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     for k in range((4-i)*2):
#         print(" ",end="")
#     for l in range(i+1,0,-1):
#         print(l,end="")
#     print()

# def pattern(n):
#     num=1
#     for i in range(n):
#         for j in range(i):
#             print(num,end="")
#             num+=1
#         print()
# pattern(4)
    

# def pattern(n):
# #    start=65
# #    middle=65
#    for i in range(n):
#         start=65
#         for j in range((n-i)-1):
#             print(" ",end="")
#         for k in range((i*2)+1):
#             print(chr(start),end="")
#             if k>=i:
#                 start-=1
#             else:
#                 start+=1
#         for l in range((n-i)-1):
#             print(" ",end="")
          
#         print()


# pattern(6)


# def palendromeDig(n):
#     num=n
#     new=0
#     for i in range(len(str(num))):
#         digit=num%10
#         new=new*10+digit
#         num//=10
#     return new==n

# print(palendromeDig(1233231))
# ar=[-1,2,3,3,4,5,-1]
# k=4
# i=0
# j=0
# sum=0
# maxsum=0
# while(j<len(ar)):
#     sum+=ar[j]
#     if ((j  - i) + 1 == k): 
#         maxsum=max(sum,maxsum)
#         sum-=ar[i]
#         i+=1
        
    
#     j+=1


# subarry=[]

# sub=[]
# k=14
# maxsum=0
# for i in range(len(ar)):
#     sum=0
#     sub=[]
#     for j in range(i,len(ar)):
#         sum+=ar[j]
#         if sum>14:
#             sum-=ar[j]
#             maxsum=max(sum,maxsum)
#             break
#         sub.append(ar[j])
#         subarry.append(sub.copy())
# print(subarry)
# print(maxsum)
# ar=[2,5,1,7,10]
# k=10
# sum=0
# maxsum=0
# length=0
# maxlength=0
# i,j=0,0
# while(j<len(ar)):
#     sum+=ar[j]
#     # length+=1
#     if sum == k:
#         maxsum = sum
#         maxlength=(j-i)+1
#         break
#     while sum > k:
#         sum-=ar[i]
#         i+=1
#     # maxsum=max(sum,maxsum)
#     if sum>maxsum:
#         maxsum=sum
#         maxlength=((j-i)+1)
#     j+=1

# print(maxsum)
# print(maxlength)


# Reverse an array
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n-1)+fib(n-2)



# def fb(m):
#     # fib_series=[]
#     for i in range(1,m+1):
#        print(fib(i),end="")

# fb(5)


# def freq(n):
#     diction = {}
    
#     for i in n:
#         diction[i] = diction.get(i,0)+1
#     maxfreq = max(diction.values())
#     for key,value in diction.items():
#         if value == maxfreq:
#             print(f"{key}:{value}")
    

        
# def buble(n):
#     for i in range(len(n)-1,0,-1):
#         for j in range(0,i):
#             if n[j] > n[j+1]:
#                 n[j],n[j+1] = n[j+1],n[j]
#     print(n)

# buble([2,3,7,1,9,5,78,3])

# def insertion(n):
#     for i in range(len(n)):
#         j = i
#         while(j > 0 and n[j] < n[j-1]):
#             n[j],n[j-1] = n[j-1],n[j]
#             j -= 1
#     print(n)
# insertion([2,3,7,1,9,5,78,3])  
# ary = [2,3,6,7,1,4,5,6]
# def checkSorted(n):
#     ascending = False
#     isSorted = True
#     if n[0] <= n[1]:
#         for i in range(len(n)):
#             for j in range(i,len(n)):
#                 if n[i] > n[j]:
#                     isSorted = False
#                     break
#                 else:
#                     ascending = True              
#     elif n[0] >= n[1]:
#         for i in range(len(n)):
#             for j in range(i,len(n)):
#                 if n[i] < n[j]:
#                     isSorted = False
#                     break              
#     print("issorted :",isSorted,"ascending :",ascending)

# print(checkSorted([2,3,3,8,4,5]))


# def isSorted(n):
#     issorted = True
#     for i in range(len(n)-1,0,-1):
#         if n[i] < n[i-1]:
#             issorted = False

#     print(issorted)
# isSorted([1,2,5,3,4,5])
# print(3%5)
               
# def rotate(nums,k):
#     k = k%len(nums)
#     # return n[k+1:] + n[:k+1]
#     nums[:] = nums[-k:] + nums [:-k]
#     return nums
# print(rotate([4,5,1],5))

# # print(3%6)
# # print(7%6)





# def moveZeros(n):
#     ar=[]
#     for i in n:
#         if i != 0:
#             ar.append(i)
#     for j in n :
#         if j == 0:
#             ar.append(j)
#     return ar

# print(moveZeros(array))

# -------------------------------------move all zeros to rightend--------------------------
# array =[1,0,2,3,0,4,0,1]
# def moveZeros(n):
    
#     i = 0
#     j=i+1
#     while( j < len(n)):
        
#         if n[i] == 0 and n[j] != 0:
#             n[i],n[j] = n[j],n[i]
#             i+=1
#             j+=1
#         elif n[i] == 0 and n[j] == 0:
#             j += 1
#         else :
#             i+=1
#             j+=1
#     return n

# ary =[[0,0,1],
# [1,2,3],
# [0,1,0,3,12],
# [0, 1, 0, 0, 2, 0, 3]]

# for i in ary:

#     print(moveZeros(i))

# ----------


# ary = [0,1,2,2,3,0,4,2]
# def  removeEle(n,v):
#     i=0
#     j=i+1
#     while(j<len(n)):
#         if n[i] == v and n[j] != v:
#             n[i],n[j] = n[j],n[i]
#             i += 1
#             j += 1
#         elif n[i] == v and n[j] == v:
#             j +=1
#         else:
#             i += 1
#             j += 1
    
#     return i
    
# print(removeEle(ary,2))
# ------------------------------------union of two arrays------------------
# using hashmap
# def union(n,m):
#     map = {}
#     for i in n :
#         map[i] = map.get(i,0)+1
#     for j in m:
#         map[j] = map.get(j,0)+1
#     return sorted(map.keys())
    
# using two pointers---------------
# def un(n,m):
#     new =[]
#     i=j=0
#     while(i < len(n) and j < len(m)):
#         if n[i] < m[j]:
#             new.append(n[i])
#             i += 1
#         elif n[i] == m[j]:
#             new.append(n[i])
#             i += 1
#             j += 1
#         else:
#             new.append(m[j])
#             j += 1
#     while(i < len(n)):
#         new.append(n[i])
#         i += 1
#     while(j < len(m)):
#         new.append(m[j])
#         j += 1
#     return new


# # print(union([1,2,3,4],[3,4,6,7]))
# print(un([1,2,3],[1,2,3,4,5,6,7]))

# def findEle(ary):
#     n = len(ary)
#     hashlist =[0] * n
#     for i in ary:
#         hashlist[i] += 1
#     for j in range(n):
#         if hashlist[j] == 0:
#             return j
#     return -1
# print(findEle([8, 2, 4, 5, 3, 7, 1]))
# def sortArray(arry):
#     for i in range(len(arry)-1):
#         min = i
#         for j in range(i,len(arry)):
#             if arry[j] < arry[min]:
#                 min = j
#         arry[min],arry[i]= arry[i],arry[min]
#     return arry

# print(sortArray([4,7,2,7,1,4]))


# ---------------------------------------------get the missing value------------------------------
# brutefource
arr = [0,1,2,4]
# def getMissing(n):
#     length = len(n)
#     hashlist = [0]*(length+2)

#     for i in range(length):
#         hashlist[n[i]] += 1

#     for j in range(1,len(hashlist)):
#         if hashlist[j] == 0:
#             return j
#     return -1
# print(getMissing(arr))

# optimal------

# def getMissing(n):
#     length= len(n)
#     expected = length *(length+1)//2
#     missing = expected - sum(n)
#     return missing

# print(getMissing(arr))



# def getMissing(n):
#     length = len(n)+1
#     hashlist = [0]*length

#     for i in n:
#         hashlist[i] += 1

#     items =[]
#     for j in range(len(hashlist)):
#         if hashlist[j] == 0:
#             items.append(j)
#     return items

# print(getMissing([1,3,4,6,7]))
    
# --------------------------max consecutive ones------------------------------
# def maxConsecutive(array):

#     i = 0
#     maximum = 0
#     sum = 0
#     for j in range(len(array)):
#         if array[j] == 1:
#             sum += 1
#             if sum > maximum:
#                 maximum = sum
#         else:
#             sum = 0
#     return maximum
    
# print(maxConsecutive([1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,1,1]))



# def appearOnes(n):
#     map = {}
#     for i in range(len(n)):
#         map[n[i]] = map.get(n[i],0) + 1

#     for key,value in map.items():
#         if value == 1:
#             return key
        
#     return -1

# print(appearOnes([4,1,2,1,2]))
# def appearOnes(n):
#     result = 0
#     for i in n:
#         result ^= i
#     return result

# print(appearOnes([4,1,2,1,2]))



# def maxSubarray(n,k):
#     j=i=0
#     sum = 0
#     maxLength = 0
#     length = 0
#     while (j < len(n)):
#         sum += n[j]
#         j += 1
#         if sum >= k:
#             length = j-i
#             maxLength = max(maxLength,length)
#             sum -= n[i]
#             i += 1
#         # else :   
#     return maxLength

# print(maxSubarray([1,2,1,1,1,1,2],4))




# total = 1
# total += -1
# print(total)

# def maxxSubarray(n,k):
#     sum = 0
#     max_length = 0
#     map = {}
#     for i in range(len(n)):
#         sum += n[i]
#         if sum == k:
#             max_length = max(max_length,i+1)

#         if (sum-k) in map:
#             length = i - map[sum-k]
#             max_length = max(length,max_length)
#         if sum not in map:
#             map[sum] = i
#     return max_length 

# print(maxxSubarray([-2,6,5,8,11],19))


# def maxsubArray(n,k):
#     i = 0
#     max_length = 0
#     sum = 0
#     for j in range(len(n)):
#         sum += n[j]
#         while(sum > k):
#             sum -= n[i]
#             i += 1
#         if sum == k:
#             length = j - i+1
#             max_length = max (length,max_length) 
#     return max_length
# print(maxsubArray([1,6,5,8,11],19))



# def twosum(n,k):
#     map = {}

#     for i,element in enumerate(n):
#         need = k - element
#         if need in map:
#             return map[need],i
#         else :
#             map[element] = i
#     return -1

# print(twosum([2,6,5,8,6],14))






