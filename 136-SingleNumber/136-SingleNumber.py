# Last updated: 8/13/2026, 8:26:18 PM
class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result ^= i

        return result
        # map = {}
        # for i in nums:
        #     map[i] = map.get(i,0)+1

        # for key,value in map.items():
        #     if value == 1:
        #         return key

        