# Last updated: 8/13/2026, 8:20:27 PM
class Solution(object):
    def findLonely(self, nums):
        from collections import Counter
        freq = Counter(nums)
        new = []
        for index, values in freq.items():
            if values == 1:
                if index + 1 not in freq and index -1 not in freq:
                    new.append(index)

        return new

        