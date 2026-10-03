class Solution(object):
    from collections import Counter
    import itertools
    def relativeSortArray(self, arr1, arr2):
        new = []
        c = Counter(arr1)
        print(c)
        for i in arr2:
            if i in c:
                new.extend([i]* c[i])
                c.pop(i)
        for i in (sorted(c)):
            new.extend([i]* c[i])

        return new

        


        


        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna