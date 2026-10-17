class Solution(object):
    def threeFibonacciSum(self, n):
        if n % 2:
            return False
        n1,n2 = 0,1
        while (n1+n2)*2 < n:
            temp = n1+n2
            n1,n2 = n2,temp
        return (n1+n2)*2 == n
        
        
        

        
            
            
        
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna