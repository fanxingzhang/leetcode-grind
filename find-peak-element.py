class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def helper(l, r):
            if l == r:
                return l
            mid = l + ((r - l) / 2)
            if nums[mid] > nums[mid + 1]:
                return helper(l, mid)
            return helper(mid + 1, r)
        return helper(0, len(nums) - 1)