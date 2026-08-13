# Last updated: 8/13/2026, 10:20:15 PM
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or len(s) == 1:
            return s
        new = [""] * numRows
        
        cycle = 2 *numRows - 2

        for i, ch in enumerate(s):
            pos = i % cycle
            row = pos if pos < numRows else cycle - pos
            new[row] += ch

        return "".join(new)
        