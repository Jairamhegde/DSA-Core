# Last updated: 8/13/2026, 8:21:02 PM
class Solution(object):
    def largestOddNumber(self, num):
        # s = num
        # i= 0
        # ndx = 0
        # for k in range(len(num)-1,-1,-1):
        #     if (int(num[k]) % 2 != 0):
        #         ndx = k
        #         break

        # while(num[i] == "0"):
        #     i += 1

        # if int(num[i:ndx+1] ) % 2 == 0:
        #     return ""
        # else:
        #     return num[i:ndx+1]

        for i in range(len(num)-1,-1,-1):
            if num[i] in {'1','3','5','7','9'}:
                return num[:i+1]
        return ""
            


        
        