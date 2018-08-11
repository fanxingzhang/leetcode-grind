class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        l = len(s)
        t = [[False for i in range(l)] for j in range(l)]
        c = 0

        for i in range(l):
            t[i][i] = True
            c += 1
            
        for i in range(l - 1):
            if s[i] == s[i + 1]:
                t[i][i + 1] = True
                c += 1

        for i in range(2, l):
            for j in range(0, l - i):
                x = j
                y = j + i
                if s[x] == s[y] and t[x + 1][y - 1]:
                    t[x][y] = True
                    c += 1
        return c
        