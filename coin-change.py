class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount in coins:
            return 1
        if amount == 0:
            return 0
        
        a = [float("inf")] * (amount + 1)
        a[0] = 0
        for c in coins:
            if c <= amount:
                a[c] = 1
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    a[i] = min(a[i], 1 + a[i - c])
        return a[-1] if a[-1] != float("inf") else -1