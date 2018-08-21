class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        a = [[0] * m for _ in range(n)]
        ret = 0
        
        for i in range(m):
            a[0][i] = int(matrix[0][i])
            if a[0][i] == 1:
                ret = 1
        for i in range(n):
            a[i][0] = int(matrix[i][0])
            if a[i][0] == 1:
                ret = 1
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == "1":
                    a[i][j] = min(a[i - 1][j], a[i][j - 1], a[i - 1][j - 1]) + 1
                    ret = max(ret, a[i][j])
        return ret * ret