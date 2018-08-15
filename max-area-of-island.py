class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def helper(i, j):
            if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i])):
                return 0
            
            if grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + helper(i + 1, j) + helper(i, j + 1) + helper(i, j - 1) + helper(i - 1, j)
            return 0
        
        r = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    r = max(helper(i, j), r)
        return r