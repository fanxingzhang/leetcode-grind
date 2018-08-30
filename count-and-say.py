class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if not n:
            return ""
        s = "1"
        for i in range(1, n):
            new = ""
            count = 0
            prev = s[0]
            for i in range(len(s)):
                if s[i] == prev:
                    count += 1
                else:
                    new += str(count) + prev
                    count = 1
                    prev = s[i]
            new += str(count) + str(prev)
            s = new
        return s
                