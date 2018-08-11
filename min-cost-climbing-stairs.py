class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        a = range(len(cost))
        a[0] = cost[0]
        a[1] = cost[1]
        for i in range(2, len(cost)):
            a[i] = min(a[i - 1], a[i  - 2]) + cost[i]
        return min(a[-1], a[-2])
                