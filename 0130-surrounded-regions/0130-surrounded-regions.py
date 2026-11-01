class Solution(object):
    from collections import deque
    def solve(self, board):
        dq = deque()
        n = len(board)
        m = len(board[0])
        convert = set()
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for i in range(n):
            if board[i][0] == "O":
                dq.append((i,0))
            if board[i][m-1] == "O":
                dq.append((i,m-1))

        for j in range(1,m-1):
            if board[0][j] == "O":
                dq.append((0,j))
            if board[n-1][j] == "O":
                dq.append((n-1,j))
        print(dq)

        while dq:
            l =len(dq)
            for _ in range(l):
                r,c = dq.popleft()
                convert.add((r,c))
                for row,col in directions:
                    rd , cd= r + row,c+col
                    if rd >=0 and rd < n and cd >= 0 and cd <m  :
                        if board[rd][cd] == "O" and (rd,cd) not in convert:
                            dq.append((rd,cd))
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    if (i,j) not in convert:
                        board[i][j] = "X"

                        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna