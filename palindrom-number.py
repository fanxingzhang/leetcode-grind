class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        a = x
        d = 0
        while a > 0:
            a = a / 10
            d += 1
        a = x
        y = 0
        for i in range(0, d):
            r = a % 10
            y += r * (10 ** (d - i - 1))
            a = a / 10
        return x == y