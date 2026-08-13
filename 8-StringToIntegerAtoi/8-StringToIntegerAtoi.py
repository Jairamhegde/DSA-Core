# Last updated: 8/13/2026, 10:20:09 PM
class Solution(object):
    def myAtoi(self, s):
        start = 0
        stop = 0
        sign = 1
        i = 0
        int_max =  2**31 -1
        int_min =  -2**31 
        while i < len(s) and s[i] ==  " ":
            i += 1
        if i >= len(s):
            return 0
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1
        start = i
        while i < len(s) and s[i].isdigit():
            i += 1
        stop = i
        if s[start:stop]:
            number = int(s[start:stop])*sign

            if number > int_max:
                return int_max
            elif number < int_min:
                return int_min
            else:
                return number
        else:
            return 0


            
        