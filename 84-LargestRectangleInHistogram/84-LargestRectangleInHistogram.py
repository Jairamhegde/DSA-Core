# Last updated: 8/13/2026, 8:26:44 PM
class Solution(object):
    def largestRectangleArea(self, heights):
        result1 = {}
        result2 = {}
        stack1 = []
        stack2 = []
        n = len(heights)
        for i in range(n):
            while stack1 and heights[stack1[-1]] >= heights[i]:
                items = stack1.pop()
                result1[items] = i
            if stack1:
                result1[i] = stack1[-1]
            stack1.append(i)
            while stack2 and heights[stack2[-1]] >= heights[i]:
                items = stack2.pop()
                
            if stack2:
                result2[i] = stack2[-1]
            else:
                result2[i] = -1
            stack2.append(i)

        for k in stack1:
            result1[k] = -1
        max_size = 0
        for j in range (n):
            
                leftmin = result2[j]
                rightmin = result1[j] if result1[j] != -1 else n

                lenght = rightmin - leftmin -1
                max_size = max(max_size,(lenght*heights[j]))
        return max_size



        

        