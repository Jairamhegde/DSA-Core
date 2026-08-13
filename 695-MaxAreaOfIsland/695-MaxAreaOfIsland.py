# Last updated: 8/13/2026, 8:22:35 PM
class Solution(object):
    def maxAreaOfIsland(self, grid):
        
        max_island=0

        def func(i,j):
            if i<0 or j<0 or i>= len(grid) or j>=len(grid[0]) or grid[i][j]==0:
                return 0
            grid[i][j]=0
            area=1
            area+=func(i+1,j)
            area+=func(i-1,j)
            area+=func(i,j+1)
            area+=func(i,j-1)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:    
                    a=func(i,j)
                    max_island=max(a,max_island)            
        return max_island

        


        