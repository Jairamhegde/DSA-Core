class Solution(object):
    def reverseDegree(self, s):
        ml = [i for i in range(26,0,-1)]
        cursum = 0
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            cursum += (ml[index] * (i+1))
        return cursum
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna