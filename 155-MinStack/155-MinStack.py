# Last updated: 8/13/2026, 8:25:47 PM
class MinStack(object):

    def __init__(self):
        self.items = []
        self.minele = []
       
   
    def push(self, value):
        if not self.minele:
            self.minele.append(value)
        
        else:
            self.minele.append(min(value,self.minele[-1]))
        return self.items.append(value)
        
    def pop(self):
        self.minele.pop()
    
        return self.items.pop()
        
    def top(self):
        return self.items[-1]
        
    def getMin(self):
        return self.minele[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()