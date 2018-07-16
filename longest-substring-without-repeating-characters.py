class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i = 0
        j = 0
        n = len(s)
        d = {}
        while i < n and j < n:
            if s[j] in d:
                i = max(d[s[j]] + 1, i)
            ans = max(j - i + 1, ans)
            d[s[j]] = j
            j += 1
        return ans