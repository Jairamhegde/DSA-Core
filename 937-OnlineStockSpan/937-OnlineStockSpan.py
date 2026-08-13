# Last updated: 8/13/2026, 8:22:15 PM
class StockSpanner(object):

    def __init__(self):
        self.stack = []
        
    def next(self, price):
      
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            items = self.stack.pop()
            span += items[1]
        self.stack.append((price,span))
        return span
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)