# Last updated: 8/13/2026, 8:27:17 PM
class Solution(object):
    def merge(self, intervals):
        new = []
        inter = sorted(intervals)

        for i in range(len(inter)):
            if not new or inter[i][0] > new[-1][1]:
                new.append(inter[i])
            else:
                if inter[i][0] <= new[-1][1]:
                    new[-1][1] = max(inter[i][1],new[-1][1])
        return new
        