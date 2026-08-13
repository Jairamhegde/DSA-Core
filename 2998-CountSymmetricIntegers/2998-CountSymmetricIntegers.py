# Last updated: 8/13/2026, 8:19:08 PM
class Solution(object):
    def countSymmetricIntegers(self, low, high):
        res = 0
        for i in range(low,high+1):
            nums = str(i)
            n = len(nums)
            if n % 2 != 0:
                continue
            else:
                
                mid = len(nums)//2
                left = nums[:mid]
                right = nums[mid:]
                l_s = sum(int(j) for j in left)
                r_s = sum(int(l) for l in right)

                if l_s == r_s:
                    res += 1
        return res
        