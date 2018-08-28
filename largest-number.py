class S(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        ret = "".join(sorted(map(str, nums), key = S))
        return "0" if ret[0] == "0" else ret