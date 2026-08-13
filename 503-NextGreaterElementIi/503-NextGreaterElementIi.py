# Last updated: 8/13/2026, 8:23:11 PM
class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1]* n
        stack = []

        for i in range(n*2):
            index = i % n
            while stack and nums[stack[-1]] < nums[index]:
                number = stack.pop()
                result[number] = nums[index]
            if i < n:
                stack.append(index)
    
        return result
            

        