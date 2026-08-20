class TimeMap:

    from collections import defaultdict
    def __init__(self):
        self.timeStamp = defaultdict(list)
        
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeStamp[key].append((timestamp,value))
    

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeStamp:
            return ""
        answer = -1
        ary = self.timeStamp[key]
        low = 0 
        high = len(ary)-1
        while low <= high:
            mid = (low + high)//2
            if ary[mid][0] <= timestamp:
                answer = mid
                low = mid + 1
            else:
                high = mid -1
        return ary[answer][1] if answer != -1 else ""

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna