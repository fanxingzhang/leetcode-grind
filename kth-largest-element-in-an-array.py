class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        temp = 0
        for i in range(len(nums) - k + 1):
            temp = heapq.heappop(nums)
        return temp