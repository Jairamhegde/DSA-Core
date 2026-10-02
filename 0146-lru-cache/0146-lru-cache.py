class Node(object):
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.mp = {}
        self.head = Node(0,0)
        self.tail = Node(-1,-1)

        self.tail.prev = self.head
        self.head.next = self.tail
        

    def remove(self,node):
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev

    def add(self,node):
        prev = self.tail.prev

        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node


    def get(self, key):
        if key not in self.mp:
            return -1
        if key in self.mp:
            node = self.mp[key]

            self.remove(node)

            self.add(node)
            return node.val

    def put(self, key, value):
        if key in self.mp:
            node = self.mp[key]
            self.remove(node)
            node.val = value 
            self.add(node)

        else:
            n = Node(key,value)
            self.mp[key] = n

            self.add(n)

        if len(self.mp)> self.capacity:
            next_node = self.head.next
            self.mp.pop(next_node.key)
            self.remove(next_node)
            






        




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna