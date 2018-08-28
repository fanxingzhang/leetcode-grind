class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        n = len(board)
        m = len(board[0])
        
        v = [[False] * m for i in range(n)]
        
        def neighbours(i, j):
            ret = []
            for a, b in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if a >= 0 and b >= 0 and a < n and b < m:
                    ret.append((a, b))
            return ret

        
        def helper(i, j, w):
            if not w:
                return True
            for a, b in neighbours(i, j):
                if not v[a][b] and board[a][b] == w[0]:
                    v[a][b] = True
                    if helper(a, b, w[1:]):
                        return True
                    v[a][b] = False
            return False        
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    v[i][j] = True
                    if helper(i, j, word[1:]):
                        return True
                    v[i][j] = False
        return False