# Last updated: 8/13/2026, 8:21:27 PM
from collections import Counter
from functools import lru_cache
from typing import List

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        cnt = list(Counter(nums).values())
        m = len(quantity)

        # sum_need[mask] = total quantity needed by customers in mask
        sum_need = [0] * (1 << m)
        for mask in range(1, 1 << m):
            bit = (mask & -mask).bit_length() - 1
            sum_need[mask] = sum_need[mask ^ (1 << bit)] + quantity[bit]

        @lru_cache(None)
        def dfs(i, mask):
            # all customers satisfied
            if mask == 0:
                return True

            # no frequencies left
            if i == len(cnt):
                return False

            # skip current frequency
            if dfs(i + 1, mask):
                return True

            # try using current frequency for some subset of remaining customers
            sub = mask
            while sub:
                if sum_need[sub] <= cnt[i]:
                    if dfs(i + 1, mask ^ sub):
                        return True
                sub = (sub - 1) & mask

            return False

        return dfs(0, (1 << m) - 1)