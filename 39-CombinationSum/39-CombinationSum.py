# Last updated: 8/13/2026, 8:27:48 PM
class Solution(object):
    def combinationSum(self, candidates, target):  
        def helper(index,target,res,current):
            if index == len(candidates):
                if target == 0:
                    res.append(current[:])
                return
            if candidates[index] <= target:
                current.append(candidates[index])
                helper(index,target-candidates[index],res,current)
                current.pop()
            
            helper(index+1,target,res,current)
            return res
        
        res = []
        current = []
        helper(0,target,res,current)
        return res

        