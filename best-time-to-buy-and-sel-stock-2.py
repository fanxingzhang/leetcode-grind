class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        buy = prices[0]
        max = 0
        sell = 0
        for i in range(1, len(prices)):
            if prices[i] < sell:
                max += sell - buy
                buy = prices[i]
                sell = 0
            elif prices[i] <= buy:
                buy = prices[i]
            else:
                sell = prices[i]

        if sell > buy:
            max += sell - buy
        return max