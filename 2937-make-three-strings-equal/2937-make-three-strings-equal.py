class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        n1 =len(s1)
        n2 =len(s2)
        n3 =len(s3)
        prev = (n1+n2+n3)
        for i in range(min(n1,n2,n3)):
            if s1[i] == s2[i] == s3[i]:
                prev -= 3
            else:
                break
        

        return prev if prev != (n1+n2+n3) else -1 

        
                    
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna