class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = -1000
        count = 0
        for i in range(len(nums)):
            if nums[i] != temp:
                nums[count] = nums[i]
                temp = nums[i]
                count = count + 1
        return count
            