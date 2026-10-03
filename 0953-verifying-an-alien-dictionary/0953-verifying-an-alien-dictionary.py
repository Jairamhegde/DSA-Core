class Solution(object):
    def isAlienSorted(self, words, order):
        m = {}
        for i in range(len(order)):
            m[order[i]] = i
        n = len(words)
        if n<2:
            return True
        l,r = 0,1
        while r < n:
            j = 0
            w1 = words[l]
            w2 = words[r]
            k,g = len(w1),len(w2)
            while j < k and j<g and w1[j] == w2[j]:
                j += 1
            if k != g :
                if j < k and j == g:
                    return False
            if j < k and j < g and m[w1[j]] > m[w2[j]]:
                return False
            
            
            l , r = l+1,r + 1
        return True

            

            

        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna