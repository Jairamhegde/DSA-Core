# Last updated: 8/13/2026, 8:25:12 PM
class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n <= 2:
            return max(nums)

        last_robed_profit = nums[0]
        previous_profit = max(nums[0],nums[1])
        for i in range(2,n):
            temp_profit = max(previous_profit,last_robed_profit + nums[i])

            last_robed_profit = previous_profit
            previous_profit = temp_profit
            
        return previous_profit