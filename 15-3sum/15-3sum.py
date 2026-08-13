# Last updated: 8/13/2026, 8:29:13 PM
class Solution(object):
    def threeSum(self, nums):
        
        n = len(nums)
        resulting_set = set()
        for i in range(n):
            stored_set = set()
            for j in range(i+1,n):
                required = 0 - (nums[i] + nums[j])
                if required in stored_set:
                    triplet = tuple(sorted((nums[i],nums[j],required)))
                    resulting_set.add(triplet)
                
                stored_set.add(nums[j])
        return list(resulting_set)

            