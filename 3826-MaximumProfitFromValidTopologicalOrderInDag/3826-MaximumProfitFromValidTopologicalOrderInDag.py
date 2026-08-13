# Last updated: 8/13/2026, 8:19:16 PM
class Solution(object):
    def maxProfit(self, n, edges, score):
        prereq = [0] * n

        for u, v in edges:
            prereq[v] |= (1 << u)

        dp = [-float("inf")] * (1<<n)
        dp[0] = 0

        for mask in range(1 << n):
            
            #Pruning - ish. Necessary to avoid TLE:
            #impossible to reach
            if dp[mask] == -float("inf"):
                continue

            seen = bin(mask).count("1")

            for nbr in range(n):
                
                #not seen yet, and have met prereqs
                if not (mask & (1 << nbr)) and (prereq[nbr] & mask) == prereq[nbr]:

                    newMask = mask | (1 << nbr)
                    val = dp[mask] + (seen+1)*score[nbr]
                        
                    #if this permutation of this combination is better, update
                    if val > dp[newMask]:
                        dp[newMask] = val
                            
        return dp[-1]
        