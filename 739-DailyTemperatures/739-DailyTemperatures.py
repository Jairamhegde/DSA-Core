# Last updated: 8/13/2026, 8:22:30 PM
class Solution(object):
    def dailyTemperatures(self, temperatures):
        next_greater = {}
        result = [0]*(len(temperatures))
        stack = []
        for index,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1] ]< temperatures[index]:
                result[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)  
        return result  

        