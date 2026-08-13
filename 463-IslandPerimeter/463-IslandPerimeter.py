# Last updated: 8/13/2026, 8:23:23 PM
class Solution(object):
    def islandPerimeter(self, grid):
        perimeter_count = 0
        visited = set()


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return self.dfs(grid,i,j,visited)
        return 0

    def dfs(self,grid,row,colums,visited):
        if row < 0 or row >= len(grid) or colums < 0 or colums >= len(grid[0]) or grid[row][colums] == 0 : 
            return 1
        if (row,colums) in visited:
            return 0
        visited.add((row,colums))
        perimeter_count = 0
        perimeter_count += self.dfs(grid,row+1,colums,visited)
        perimeter_count += self.dfs(grid,row-1,colums,visited)
        perimeter_count += self.dfs(grid,row,colums+1,visited)
        perimeter_count += self.dfs(grid,row,colums-1,visited)
        return perimeter_count



        