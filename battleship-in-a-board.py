class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == 'X':
                    if i == 0 and j == 0:
                        count += 1
                    elif i > 0 and j == 0 and board[i - 1][j] == ".":
                        count += 1
                    elif j > 0 and i == 0 and board[i][j - 1] == ".":
                        count += 1   
                    elif board[i-1][j] == '.' and board[i][j-1] == '.':
                        count += 1
        return count