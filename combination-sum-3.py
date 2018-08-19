class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates = range(1, 10)
        def helper(a, t, s):
            if t == 0 and len(s) == k:
                ret.append(s)
                return
            if len(s) >= k:
                return
            for i in range(len(a)):
                if a[i] > t:
                    break
                else:
                    helper(a[i + 1:], t - a[i], s + [a[i]])
        helper(candidates, n, [])
        return ret