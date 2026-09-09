class Solution(object):
    def twoSum(self, numbers, target):
        mp ={}
        for i in range(len(numbers)):
            needed = numbers[i] - target
            need2 = needed*-1
            if needed in mp:
                if needed + numbers[i] == target:
                    return [mp[needed]+1,i+1]
            if need2 in mp:
                if need2 + numbers[i] == target:
                    return [mp[need2]+1,i+1]
            if numbers[i] not in mp:
                mp[numbers[i]] = i
        return []

             
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna