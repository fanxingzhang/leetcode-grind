class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int(
        """
        
        
        digits = len(str(abs(x)))
        sol = 0
        ori = abs(x)
        for i in range(0, digits):
            d = ori % 10
            sol += d * (10 ** (digits - 1 - i))
            if sol > 2 ** 31 - 1:
                return 0
            ori = ori / 10
            
        return sol if x > 0 else sol * -1