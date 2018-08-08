class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l =  len(s)
        s = list(s)
        for i in range(l/2):
            s[i], s[l - i - 1] = s[l - i - 1], s[i]
        return "".join(s)