class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def helper(s):
            for i in range(len(s) / 2):
                if s[i] != s[-i - 1]:
                    return False
            return True
        
        l = 0
        r = len(s) - 1
        while r > l:
            if s[r] == s[l]:
                l += 1
                r -= 1
            else:
                return helper(s[l:r]) or helper(s[l + 1: r + 1])
        return True