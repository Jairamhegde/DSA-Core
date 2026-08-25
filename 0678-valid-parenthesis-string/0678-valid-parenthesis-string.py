class Solution(object):
    def checkValidString(self, s):
        stack = []
        bmap = {']':'[',')':'(','{':'}'}
        opens = {"{","[","("}
        stack2 = []
        starcount = 0
        for i in range(len(s)):
            ch = s[i]
            if  ch in opens:
                stack.append(i)
            elif  ch == "*":
                stack2.append(i)
    
            else:
                if not stack or s[stack[-1]] != bmap[ch]:
                    if stack2 and stack2[-1] < i:
                        stack2.pop()
                        continue
                    else:
                        return False
                else:
                    stack.pop()
        
        while stack and stack2 and stack2[-1] > stack[-1]:
            stack2.pop()
            stack.pop()
        if stack:
            return False

        
        return True
            
        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna