class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        a = [float("inf")] * n
        p = []
        i = 1
        while i * i <= n:
            a[i * i - 1] = 1
            p.append(i * i)
            i += 1

        if a[n - 1] != float("inf"):
            return a[n - 1]
        
        for i in range(1, n + 1):
            for prime in p:
                if prime >= i:
                    break
                a[i - 1] = min(a[i - 1], a[prime - 1] + a[i - prime - 1])  
        return a[n - 1]