class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        f = False
        for c in s[::-1]:
            if c == ' ' and f:
                break
            elif c != ' ':
                f = True
                r += 1
        return r
