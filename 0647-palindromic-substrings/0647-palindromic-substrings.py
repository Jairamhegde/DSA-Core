class Solution(object):
    def countSubstrings(self, s):
        max_substrings = 0
        n = len(s)
        for i in range(n):
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                max_substrings += 1
                l -= 1
                r += 1

            l = i
            r = i+1
            while l >= 0 and r < n and s[l] == s[r]:
                max_substrings += 1
                l -= 1
                r += 1
        return max_substrings


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna