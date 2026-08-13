# Last updated: 8/13/2026, 8:27:39 PM
class Solution(object):
    def trap(self,height):
        n = len(height)
        stk1 = [0]*n
        stk2 = [0]*n
        
        for i in range(1,n):
            if i == 1:
                stk1[i] = height[i-1]
            else:
                stk1[i] = max(stk1[i-1],height[i-1])
        for j in range(n-2,-1,-1):
            if j == n-2:
                stk2[j] = height[j+1]
            else:
                stk2[j] = max(stk2[j+1],height[j+1])
        total_water = 0
        for k in range(n):
            value = (min(stk1[k],stk2[k])- height[k])
            total_water += value if value >= 0 else 0
        return total_water

            



        
        