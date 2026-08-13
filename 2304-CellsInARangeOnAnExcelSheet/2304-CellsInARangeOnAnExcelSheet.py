# Last updated: 8/13/2026, 8:20:15 PM
class Solution(object):
    def cellsInRange(self, s):
        col1 = s[0]
        col2 = s[3]
        row1 = int(s[1])
        row2 = int(s[4])
        new = []
        val1 = ord(col1)
        val2 = ord(col2)
        for i in range(val1,val2+1):
                count = row1
                while count <= row2:
                        new.append(chr(i)+str(count))
                        count += 1
        return new
        