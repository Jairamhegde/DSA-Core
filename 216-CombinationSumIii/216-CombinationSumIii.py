# Last updated: 8/13/2026, 8:24:57 PM
class Solution(object):
    def combinationSum3(self, k, n):
        
        def helper(new,current,index,currentSum):
            
            if currentSum > n:
                return
            if len(current[:]) > k:
                return
            if len(current) == k and currentSum == n:
                new.append(current[:])
                return
            for i in range(index,10):
                if currentSum > n:
                    break
                current.append(i)
                currentSum += i
                helper(new,current,i+1,currentSum)
                item = current.pop()
                currentSum -= item
        new = []      
        helper(new,[],1,0)
        return new