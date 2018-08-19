class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        
        d = {}
        for f in flights:
            if f[0] in d:
                d[f[0]].append(f[1:3])
            else:
                d[f[0]] = [f[1:3]]
        
        q = [[src, 0, K]]
        ret = float("inf")
        while q:
            curr = q.pop(0)
            curr_d = curr[1]
            curr_stop = curr[2]
            if curr_stop < 0 or curr[0] not in d:
                continue
            for f in d[curr[0]]:
                new_d = curr_d + f[1]
                if f[0] == dst:
                    ret = min(ret, new_d)
                elif new_d < ret:
                    q.append([f[0], new_d, curr_stop - 1])
        return ret if ret != float("inf") else -1
        