class Solution(object):
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                left = grid[i][j-1] if j != 0 else float('inf')
                right = grid[i-1][j] if i != 0 else float('inf')

                grid[i][j] = grid[i][j] + min(left,right)
        return grid[-1][-1]

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna