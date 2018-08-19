class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        a = None
        for n in nums:
            if c == 0:
                a = n
            c += 1 if n == a else -1
        return a