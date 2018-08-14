class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ret = []
        start = 0
        prev = s[0]
        for i, c in enumerate(s):
            if c != prev:
                if i - start >= 3:
                    ret.append([start, i - 1])
                start = i
                prev = c
        if i + 1 - start >= 3:
            ret.append([start, i])
        return ret