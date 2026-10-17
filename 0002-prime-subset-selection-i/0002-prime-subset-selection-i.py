class Solution(object):
    def maxPrimes(self, n, s):
        prime_dp = [True]* (n+1)
        selected_prime= []
        total = 0
        prime_dp[0],prime_dp[1] = False,False
        i = 2
        while i  <= n and total < s:
            if prime_dp[i]:
                if total + i <= s:
                    total += i
                    selected_prime.append(i)
                    for j in range(i*i,n+1,i):
                        prime_dp[j] = False
                else:
                    break
            i += 1
        return selected_prime
        


                    
            
        
        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna