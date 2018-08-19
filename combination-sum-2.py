class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates = sorted(candidates)
        def helper(a, t, s):
            if t == 0:
                ret.append(s)
                return
            for i in range(len(a)):
                n = a[i]
                if i > 0 and n == a[i - 1]:
                    continue
                if n > t:
                    break
                else:
                    helper(a[i + 1:], t - n, s + [n])
        helper(candidates, target, [])
        return ret