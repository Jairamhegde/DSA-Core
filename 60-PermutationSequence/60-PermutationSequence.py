# Last updated: 8/13/2026, 8:27:09 PM
class Solution(object):
    def getPermutation(self, n, k):
        numbers = []

        fact = 1

        for i in range(1,n):
            fact *= i
            numbers.append(i)
        numbers.append(n)
        ans = ""
        k -= 1
        while numbers:
            ans += str(numbers[k//fact])
            numbers.remove(numbers[k//fact])

            if not numbers:
                break
            k %= fact
            fact //= len(numbers)
        return ans

        