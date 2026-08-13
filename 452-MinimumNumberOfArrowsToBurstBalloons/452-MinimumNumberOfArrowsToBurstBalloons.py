# Last updated: 8/13/2026, 8:23:27 PM
class Solution(object):
    def findMinArrowShots(self, points):
        point = sorted(points,key= lambda x:x[1])
        end = float('-inf')

        count = 0
        for i in range(len(points)):
            if end < point[i][0]:
                end = point[i][1]
                count += 1
            else:
                end = min(end,point[i][1])

        return count
        