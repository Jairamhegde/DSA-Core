# Last updated: 8/13/2026, 8:23:38 PM
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        interval = sorted(intervals)
        end = float('-inf')
        count = 0
        for i in range(len(interval)):
            if end <= interval[i][0]:
                end = interval[i][1] 
            else:
                end = min(end,interval[i][1])
                count += 1
        return count

        