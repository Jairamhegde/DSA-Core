# Last updated: 8/13/2026, 8:27:35 PM
class Solution(object):
    def permute(self, nums):
        new = []
        n = len(nums)
        def helper(index):
            if index == n:
                new.append(nums[:])
                return
            for i in range(index,n):
                nums[i],nums[index] = nums[index],nums[i]
                helper(index+1)
                nums[index] ,nums[i] = nums[i],nums[index]

        helper(0)
        return new
            


            
        