class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = collections.defaultdict(int)
        for c in s:
            d[c] += 1
        m = ''
        a = float("inf")
        for c in d:
            if d[c] < k:
                a = d[c]
                m = c
                
        if a >= k:
            return len(s)
        b = s.split(m)
        ret = 0
        for x in b:
            ret = max(ret, self.longestSubstring(x, k))
        return ret