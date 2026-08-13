# Last updated: 8/13/2026, 8:24:49 PM
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])

            if len(seen) > k:
                seen.remove(nums[i-k])
        return False

        