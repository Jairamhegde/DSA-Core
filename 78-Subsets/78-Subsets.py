# Last updated: 8/13/2026, 8:26:49 PM
class Solution(object):
    def subsets(self, nums):
        new = []
        current = []
        def helper(new,current,index):
            if index == len(nums):
                new.append(current[:])
                return
            current.append(nums[index])
            helper(new,current,index+1)

            current.pop()
            helper(new,current,index+1)
            return new

        helper(new,current,0)
        return new
        