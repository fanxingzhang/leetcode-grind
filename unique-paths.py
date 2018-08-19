class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        
        a = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    a[i][j] = 1
                else:
                    a[i][j] = a[i - 1][j] + a[i][j - 1]
        return a[m - 1][n - 1]