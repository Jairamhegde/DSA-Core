# Last updated: 8/13/2026, 8:19:13 PM
class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        dig = purchaseAmount % 10
        if dig >= 5:
            amount = 10 - dig
            return 100 - (purchaseAmount + amount)
        else:
            return 100 - (purchaseAmount - dig)