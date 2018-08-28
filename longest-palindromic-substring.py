class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            a[i][i] = True
        x = y = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                a[i][i + 1] = True
                x, y = i, i + 1
        
        for i in range(2, len(s)):
            for j in range(0, len(s) - i):
                if s[j] == s[j + i] and a[j + 1][j + i - 1]:
                    a[j][j + i] = True
                    x, y = j, j + i
        return s[x:y + 1]