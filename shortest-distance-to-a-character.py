class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        ret = [len(s)] * len(s)
        
        for i in range(len(s)):
            if s[i] == c:
                ret[i] = 0
        
        for i in range(1, len(s)):
            ret[i] = min(ret[i], ret[i - 1] + 1)
        
        for i in range(len(s) - 2, -1, -1):
            ret[i] = min(ret[i], ret[i + 1] + 1)
        
        return ret