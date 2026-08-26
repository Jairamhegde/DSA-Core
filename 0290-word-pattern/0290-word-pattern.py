class Solution(object):
    def wordPattern(self, pattern, s):
        
        map1 = {}
        map2 = {}
        sl = s.split(" ")
        if len(pattern) != len(sl):
            return False
        for i in range(len(pattern)):
            if sl[i] not in map2:
                map2[sl[i]] = pattern[i]
            if pattern[i] not in map1:
                if map2[sl[i]] == pattern[i]:
                    map1[pattern[i]] =sl[i]
                else:
                    return False
            else:
                if map1[pattern[i]] == sl[i]:
                    continue
                else:
                    return False
        return True

            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna