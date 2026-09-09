class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)
        left,right = 0,n-1
        while left <= right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left+1,right+1]
            if current > target:
                right -= 1
            elif current < target:
                left += 1
        return []

             
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna