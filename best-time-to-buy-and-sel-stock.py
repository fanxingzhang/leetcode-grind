class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        b = prices[0]
        max = 0
        for i in range(1, len(prices)):
            if prices[i] - b > max:
                max = prices[i] - b
            if prices[i] < b:
                b = prices[i]
        return max