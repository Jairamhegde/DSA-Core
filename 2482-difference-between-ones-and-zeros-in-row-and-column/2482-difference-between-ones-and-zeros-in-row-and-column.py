class Solution(object):
    def onesMinusZeros(self, grid):
       
        n = len(grid)
        m = len(grid[0])
        rows = [[0,0]for _ in range(n)]
        cols = [[0,0] for _ in range(m)]
      
        for i in range(n):
            for j in range(m):
                value = grid[i][j]
                
                rows[i][value] = rows[i][value]+1
                cols[j][value] = cols[j][value]+1
            
        mygrid = [[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                mygrid[i][j] = (
                   rows[i][1] + cols[j][1]- rows[i][0]- cols[j][0]
                   )
    
        return mygrid
       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna