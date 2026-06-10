n=-1234

# def reverse(count,n):
#     if n==0:
#         return count
#     f=n%10
#     count=count*10+f
#     return reverse(count,n//10)
# print++(reverse(0,1234))

def count(n):
    if n<=0:
        return 0
    return 1+count(n//10)

print(count(n=n))

def reverse(n):
    if n<10:
        return n
    last=n%10
    remaining=n//10
    digit_count=count(remaining)
    return last*(10**digit_count)+reverse(remaining)

print(reverse(n=n))
