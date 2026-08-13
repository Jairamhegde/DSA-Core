# Last updated: 8/13/2026, 8:24:35 PM
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        from collections import deque
        new = []
        queue = deque()
        n = len(nums)
        left = 0
        for i in range(n):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

            if queue[0] < left:
                queue.popleft()

            if i-left+1 >= k:
                new.append(nums[queue[0]])
                left += 1
           

        return new


        
            

        