# Last updated: 8/13/2026, 8:22:06 PM
class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        new = []
        for i in range(rows):
            for j in range(cols):
                current =[i,j]
                new.append(current)
        new = sorted(new,key = lambda x :abs(rCenter - x[0]) + abs(cCenter-x[1]))
        return new
        