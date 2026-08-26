class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hashtable = [0]*26
        for j in magazine:
            index = ord(j) - ord('a')
          
            
            hashtable[index] += 1

        for k in ransomNote:
            index = ord(k) - ord('a')
            if hashtable[index] == 0:
                return False
            hashtable[index] -= 1
        return True

          
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna