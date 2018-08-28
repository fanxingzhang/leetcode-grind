class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        l = len(gas)
        diff = []
        for i in range(l):
            diff.append(gas[i] - cost[i])
        if sum(diff) < 0:
            return -1
        m, s = float("inf"), diff[0]
        
        ret = 0
        if l > 1:
            for i in range(0, l):
                s += diff[i]
                if s < m:
                    m = s
                    ret = i + 1
        if ret >= l:
            ret = 0
        return ret