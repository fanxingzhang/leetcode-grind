class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = {}
        s = n
        while True:
            s = sum(int(i) ** 2 for i in str(s))
            if s == 1:
                return True
            if s in d:
                return False
            d[s] = 1