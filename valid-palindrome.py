class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.lower()
        l = 0
        r = len(s) - 1
        while r > l:
            if not ((s[l] <= 'z' and s[l] >='a') or (s[l] >= '0' and s[l] <= '9')):
                l += 1
            elif not ((s[r] <= 'z' and s[r] >='a') or (s[r] >= '0' and s[r] <= '9')):
                r -= 1
            elif s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True