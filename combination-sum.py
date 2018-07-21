class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        r = []
        def helper(t, s):
            if t == 0:
                r.append(s)
                return
            for n in candidates:
                if n > t:
                    break
                if s and n < s[-1]:
                    continue
                else:
                    helper(t - n, s + [n])
        helper(target, [])
        return r