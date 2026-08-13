# Last updated: 8/13/2026, 10:20:06 PM
class Solution(object):
    def isPalindrome(self, x):
        new = 0
        k = x
        while k > 0:
            dig = k % 10
            new = new * 10 + dig
            k //= 10

        return new == x
        