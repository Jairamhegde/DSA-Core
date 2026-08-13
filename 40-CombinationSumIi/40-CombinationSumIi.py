# Last updated: 8/13/2026, 8:27:43 PM
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
   
        def helper(new,current,index,currSum):
            if currSum == target:
                new.append(current[:])
                return

            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if currSum+candidates[i] > target:
                    break
                currSum += candidates[i]
                current.append(candidates[i])
                helper(new,current,i+1,currSum)

                item =current.pop()
                currSum -= item

            
        new = []
        helper(new,[],0,0)
        return new