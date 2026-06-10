# class Solution(object):
def count(n):
    if n<=0:
        return 0
    return 1+count(n//10)
def reverse(x):
    if x<10:
        return x
    last=x%10
    digit_count=count(x//10)
    return last*(10**digit_count)+reverse(x//10)
print(reverse(1234))

        