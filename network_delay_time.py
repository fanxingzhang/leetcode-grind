class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        d = collections.defaultdict(list)
        for u, v, w in times:
            d[u].append((v, w))
        visited = {}
        dist = {n : float("inf") for n in range(1, N + 1)}
        dist[K] = 0
        while True:
            curr = -1
            curr_dist = float("inf")
            for i in range(1, N + 1):
                if dist[i] < curr_dist and i not in visited:
                    curr = i
                    curr_dist = dist[i]
                            
            if curr < 0:
                break
            
            visited[curr] = 1
                            
            for v, w in d[curr]:
                dist[v] = min(dist[v], curr_dist + w)
        ret = max(dist.values())
        return ret if ret != float("inf") else -1
                    