# Last updated: 8/13/2026, 8:26:35 PM
class Solution(object):
    def subsetsWithDup(self, nums):
        new = []
        nums.sort()
        
        def helper(new,current,index):
            new.append(current[:])
            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                helper(new,current,i+1)
                current.pop()
        
        helper(new,[],0)
        return new

                