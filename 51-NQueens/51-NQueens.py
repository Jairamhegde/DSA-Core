# Last updated: 8/13/2026, 8:27:22 PM
class Solution(object):
    def solveNQueens(self, n):
        
    # This represents our current chess board
        board = [["."] * n for _ in range(n)]
        
        # This will store all valid board configurations
        results = []
        
        def issafe(row, column):
            # Check if there is a queen in the same column above this row
            for i in range(row):
                if board[i][column] == "Q":
                    return False
                    
            # Check upper-left diagonal
            r, c = row, column
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
                
            # Check upper-right diagonal
            r, c = row, column
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1
                
            return True

        def helper(index):
            # Base case: If we reach row 'n', we successfully placed 'n' queens
            if index == n:
                # Join the lists of characters into strings to match standard formatting
                results.append(["".join(r) for r in board])
                return
            
            # Try placing a queen in each column of the current row (index)
            for i in range(n):
                if issafe(index, i):
                    board[index][i] = "Q"       # Place the queen
                    helper(index + 1)           # Move to the NEXT row
                    board[index][i] = "."       # Backtrack: remove the queen to try the next column
                    
        # Start the recursion at row 0
        helper(0)
        
        return results

# Example usage:
# print(nqueens(4))