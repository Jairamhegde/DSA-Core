array=[7,22,5,9,2,12,11,8]
# for i in range(len(array)-2):
#     min = i
#     for j in range(i,len(array)):
#         if array[j] < array[min]:
#             min = j
#     temp = array[i]
#     array[i] = array[min]
#     array[min] = temp
# print(array)


# def bubleSort(n):
#     length=len(n)
#     isSwaped=0
#     for i in range(length-1,0,-1):
#         for j in range(0,i):
#             if n[j] > n[j+1]:
#                 n[j],n[j+1] = n[j+1], n[j]
#                 isSwaped=1
#         print("runs")
#         if isSwaped == 0:
#             break
#     return n
# ar2=[1,2,3,4,5]
# print(bubleSort(array))


# def insertionSort(n):
#     for i in range(1,len(n)):
#         j=i
#         while(j > 0 and n[j-1] > n[j]):
#             n[j-1],n[j] = n[j],n[j-1]
#             j -= 1
#     return n
# print(insertionSort(array))