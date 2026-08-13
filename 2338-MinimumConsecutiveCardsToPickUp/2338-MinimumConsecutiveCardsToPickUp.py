# Last updated: 8/13/2026, 8:20:11 PM
class Solution(object):
    def minimumCardPickup(self, cards):
        dp = {}
        min_len = float("inf")
        for i in range(len(cards)):
            if cards[i] in dp :
                min_len = min (min_len, i - dp[cards[i]] + 1)
                dp[cards[i]] = i
            else:
                dp[cards[i]] = i
        return -1 if min_len == float("inf") else min_len
        