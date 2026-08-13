# Last updated: 8/13/2026, 8:24:44 PM
class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                item = self.stack1.pop()
                self.stack2.append(item)
        items = self.stack2.pop()
        return items
        

    def peek(self):
        if not self.stack2:
            while self.stack1:
                item = self.stack1.pop()
                self.stack2.append(item)
        return self.stack2[-1]
    def empty(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        else:
            return False
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()