# num=234517
# n=num
# count=0
# while (n>0):
#     n=n//10
#     count+=1
# print("The number of digits :",count)

# from math import *

# def countlog(logg):
#     return int(log10(logg)+1)

# print(countlog(341882323))

# ---------------palendrome------------

# n=12333421

# num=n
# num=0
# while (num>0):
#     dig=num%10
#     num=num*10+dig
#     num=int(num//10)
    
# print("palendrom" if num==n else "Not a palendrome")


# ----------------armstrong------------

# n=1534

# def isArmstrong(numm):
#     num=numm
#     count=0
#     # num=num
#     summ=0
#     while(num>0):
#         count+=1
#         num=num//10
#     num=numm
#     while(num>0):
#         dig=num%10
#         summ=summ+(dig**count)
#         num=num//10
#     return (summ==numm)
# print("Armstrong " if isArmstrong(n) else "Not Armstrong")
# print("Armstrong " if isArmstrong(n) else "Not a armstrong" )

# ---------------------------------factor of a number-----------------------

from math import sqrt
num=25
# half=num//2
# factors=[]
# for i in range(1,half+1):
#     if (num %i==0):
#         factors.append(i)
# factors.append(num)
# print(factors)
factors=[]
for i in range(1,int(sqrt(num))+1):
    if (num%i==0):
        n=num/i
        factors.append(int(n))
        if not(i==n):
            factors.append(int(i))

print(sorted(factors))