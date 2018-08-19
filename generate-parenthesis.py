class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        ret = []
        def helper(a, b, s):
            if a == 0 and b == 0:
               ret.append(s)
            if a > 0:
                helper(a - 1, b, s + "(")
            if a < b and b > 0:
                helper(a, b - 1, s + ")")
        
        helper(n, n, "")
        return ret