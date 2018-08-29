class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        v = {}
        
        def helper(s):
            if not s:
               return 1
            if len(s) == 1 and s != "0":
                return 1
            if s in v:
                return v[s]
            ret = 0
            if s[0] != "0":
                ret += helper(s[1:])
                if int(s[0:2]) <= 26:
                    ret += helper(s[2:])
            v[s] = ret
            return ret
        
        return helper(s)
        