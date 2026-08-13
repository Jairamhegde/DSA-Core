# Last updated: 8/13/2026, 8:22:20 PM
class Solution(object):
    def rotateString(self, s, goal):
        newstring = s + s
        i = 0
        j = len(s)
        while(j < len(newstring)):

            if newstring[i : j] == goal:
                return True
            i += 1
            j += 1
        return False


        

        