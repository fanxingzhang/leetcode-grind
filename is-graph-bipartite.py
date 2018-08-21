class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        d = {}
        def helper(n, b):
            d[n] = b
            for i in graph[n]:
                if i in d:
                    if d[i] == b:
                        return False
                elif not helper(i, not b):
                    return False
            return True
        for i in range(len(graph)):
            if i not in d:
                if not helper(i, True):
                    return False
        return True
