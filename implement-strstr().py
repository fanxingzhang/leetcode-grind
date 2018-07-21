class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        l = len(needle)
        a = 0
        b = a + l
        while b < len(haystack) + 1:
            if haystack[a:b] == needle:
                return a
            a += 1
            b += 1
        return -1