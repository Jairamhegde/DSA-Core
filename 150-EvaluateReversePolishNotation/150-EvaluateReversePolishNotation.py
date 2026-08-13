# Last updated: 8/13/2026, 8:26:01 PM
class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                item = stack.pop()
                stack[-1] = stack[-1] + item
            elif tokens[i] == "-":
                item = stack.pop()
                stack[-1] = stack[-1] - item
            elif tokens[i] == "/":
                item = stack.pop()
                stack[-1] = int(stack[-1] / float(item))
            elif tokens[i] == "*":
                item = stack.pop()
                stack[-1] = int(stack[-1] * item)
            else:
                stack.append(int(tokens[i]))
        return stack[0]
        