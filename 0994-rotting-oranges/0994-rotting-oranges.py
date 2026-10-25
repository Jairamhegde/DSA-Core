class Solution(object):
    from collections import deque,defaultdict
    def orangesRotting(self, grid):
        n = len(grid)
        m = len(grid[0])
        temp = grid[:]
        dq = deque()
        visited = defaultdict()
    
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        time = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    dq.append((i,j))

        while dq:
            l = len(dq)

            found = False
            for _ in range(l):
                r,c = dq.popleft()
                for rd,cd in directions:
                    row,col = r+rd,c+cd
                    if 0<=row< n and 0 <= col < m and temp[row][col] == 1:
                        dq.append((row,col))
                        temp[row][col] = 2
                        found = True
            if found:
                time += 1

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 1:
                    return -1
        return time
        
        

                


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna