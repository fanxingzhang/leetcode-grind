class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d = collections.defaultdict(int)
        for i in range(len(s)):
            d[s[i]] += 1
            d[t[i]] -= 1
        for c in d:
            if d[c] != 0:
                return False
            
        return True