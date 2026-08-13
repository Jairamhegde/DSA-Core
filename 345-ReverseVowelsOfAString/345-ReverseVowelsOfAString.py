# Last updated: 8/13/2026, 8:24:06 PM
class Solution(object):
    def reverseVowels(self, s):
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        new = list(s)
        print(new)
        n = len(new)
        i = 0
        j = len(new)-1
        while i < j:
            while i < j and new[i] not in vowels:
                i += 1
            while j > i and new[j] not in vowels:
                j -= 1
            new[i],new[j] = new[j],new[i]
            i += 1
            j -= 1
        return "".join(new)

            


        