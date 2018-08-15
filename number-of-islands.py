class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def helper(i, j):
            if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i])):
                return
            
            if grid[i][j] == '1':
                grid[i][j] = '0'
                helper(i + 1, j)
                helper(i, j + 1)
                helper(i, j - 1)
                helper(i - 1, j)
        
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    c += 1
                    helper(i, j)
        return c