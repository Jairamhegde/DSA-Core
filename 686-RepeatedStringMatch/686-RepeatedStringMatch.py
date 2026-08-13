# Last updated: 8/13/2026, 8:22:38 PM
class Solution(object):
    def repeatedStringMatch(self, a, b):
        def check(a,b):
            mod = 10**9+7
            currentSum = 0
            hashcode = 0
            d = {
                "a":1,
                "b":2,
                "c":3,
                "d":4,
                "e":5,
                "f":6,
                "g":7,
                "h":8,
                "i":9,
                "j":10,
                "k":11,
                "l":12,
                "m":13,
                "n":14,
                "o":15,
                "p":16,
                "q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26
            }
            base = 26
            highiestpower = pow(base,len(a) ,mod)
            
            for i in range(len(a)):
                val = d[a[i]]
                hashcode = (hashcode * base + val)%mod

            j = 0
            k = 0
            while j < len(b):
                val = d[b[j]]
                currentSum = (currentSum * base + val)%mod

                if j - k+1 > len(a):
                    val = d[b[k]]
                    currentSum =( (currentSum - val * highiestpower)%mod)
                    k += 1
                
                if j - k + 1 == len(a):
                    if currentSum == hashcode:
                        return True
                j += 1
            
            return False


        minrepeat = (len(a) + len(b) -1)//len(a)

        if check(b,a*minrepeat):
            return minrepeat
        if check(b,a*(minrepeat+1)):
            return minrepeat + 1
        return -1


        


        


        

