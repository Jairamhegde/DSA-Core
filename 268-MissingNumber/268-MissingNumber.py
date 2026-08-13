# Last updated: 8/13/2026, 8:24:23 PM
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums) 
        summ = n*(n+1)//2
        print(summ)
        arraysum = 0
        for i in nums:
            arraysum += i 

        missing = summ - arraysum
        return missing       