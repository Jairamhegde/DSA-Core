# Last updated: 8/13/2026, 8:25:56 PM
class Solution(object):
    def maxProduct(self, nums):
        max_prod = nums[0]
        n = len(nums)
        prod = 1
        for i in range(n):
            prod *= nums[i]
            max_prod = max(max_prod,prod)
            if prod == 0:
                prod = 1
        prod = 1
        for j in range(n-1,-1,-1):
            prod *= nums[j]
            max_prod = max(max_prod,prod)
            if prod == 0:
                prod = 1
        return max_prod

            
            

        