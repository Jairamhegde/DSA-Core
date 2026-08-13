# Last updated: 8/13/2026, 8:26:52 PM
class Solution(object):
    from collections import Counter
    def minWindow(self, s, t):
        need = Counter(t)
        required  = len(need)

        window = {}
        have = 0

        min_len = float('inf')
        left = 0
        best_left = 0

        for i in range(len(s)):
            ch = s[i]
            window[ch] = window.get(ch,0)+1
            if ch in need and window[ch] == need[ch]:
                have += 1
            
            while have == required:
                left_ch = s[left]

                if (i - left + 1) < min_len:
                    min_len =( i - left + 1)
                    best_left = left
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1
                left += 1
        return "" if min_len == float('inf') else s[best_left: best_left + min_len]

                    

            

        
