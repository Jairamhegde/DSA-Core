# Last updated: 8/13/2026, 10:20:19 PM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        from collections import defaultdict
        dp = defaultdict(int)
        maxlen = 0
        left = 0
        for right in range(len(s)):
            dp[s[right]] += 1
            
            while dp[s[right]] > 1:
                dp[s[left]] -= 1
                left += 1
            maxlen = max(maxlen,right-left + 1)
        return maxlen
        
            


                
            




        