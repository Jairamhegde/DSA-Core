class Solution(object):
    from collections import deque
    def updateMatrix(self, mat):
        n = len(mat)
        m = len(mat[0])
        visited = set()
        copy = mat[:]
        dq = deque()

        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    dq.append((i,j))
        count = 1
        while dq:
            lenght = len(dq)
            for _ in range(lenght):
                r,c = dq.popleft()
                for row,col in direction:
                    rd,cd = r + row,col + c
                    if rd >=0 and rd < n and cd>=0 and cd<m and (rd,cd) not in visited and mat[rd][cd] == 1:
                        copy[rd][cd] = count
                        visited.add((rd,cd))
                        dq.append((rd,cd))
            count += 1
        return copy




                



        


       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna