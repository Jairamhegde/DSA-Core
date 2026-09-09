class Solution(object):
    def intersection(self, nums1, nums2):
        num1 = set(nums1)
        num2 = set(nums2)
        answ = []
        for i in num1:
            if i in num2:
                answ.append(i)
        return answ
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna