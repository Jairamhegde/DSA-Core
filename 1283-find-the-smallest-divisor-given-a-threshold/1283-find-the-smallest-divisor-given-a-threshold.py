class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(nums,threshold,k):
            sum_val = 0
            for j in range(len(nums)):
                sum_val += math.ceil(nums[j]/k)
            if sum_val <= threshold:
                return True
            else:
                return False
        max_val = max(nums)
        low , high = 1,max_val
        answer = max_val
        while low <= high:

            mid = (low + high )//2
            res = check(nums,threshold,mid)
            
            if res:
                answer = mid
                high = mid -1
            else:
                low = mid + 1
        return answer


        