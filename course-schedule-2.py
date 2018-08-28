class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        d = collections.defaultdict(list)
        d2 = collections.defaultdict(int)
        d3 = [True] * numCourses
        for p in prerequisites:
            d[p[1]] += [p[0]]
            d2[p[0]] += 1
            d3[p[0]] = False
        q = []
        for i in range(numCourses):
            if d3[i]:
               q.append(i)
        ret = []
        while q:
            n = q.pop(0)
            ret.append(n)
            for c in d[n]:
                d2[c] -= 1
                if d2[c] <= 0:
                    q.append(c)
        if len(ret) == numCourses:
            return ret
        else:
            return []