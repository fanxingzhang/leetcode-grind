class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        n = len(board)
        m = len(board[0])

        def helper(i, j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return
            if board[i][j] == 'O':
                board[i][j] = '-'
                for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    helper(x, y)
                    
        for i in range(m):
            helper(0, i)
            helper(n- 1, i)
        for i in range(n):
            helper(i, 0)
            helper(i, m - 1)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '-':
                    board[i][j] = 'O'