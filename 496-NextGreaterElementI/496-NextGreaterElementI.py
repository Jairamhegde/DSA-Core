# Last updated: 8/13/2026, 8:23:15 PM
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greter = {}
        for num in nums2:

            while stack and stack[-1] < num:
                number = stack.pop()
                next_greter[number] = num
            stack.append(num)
        for i in stack:
            next_greter[i] = -1
        return [next_greter[j] for j in nums1]
           
        
            

        