class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0:
            return(0)
        a = [[0] * n for _ in range(m)]
            
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if i == 0 and j == 0:
                    a[i][j] = grid[0][0]
                elif i == 0:
                    a[i][j] = grid[i][j] + a[i][j - 1]
                elif j == 0:
                    a[i][j] = grid[i][j] + a[i - 1][j]
                else:
                    a[i][j] = min(a[i - 1][j], a[i][j - 1]) + grid[i][j]
                
        return a[-1][-1]