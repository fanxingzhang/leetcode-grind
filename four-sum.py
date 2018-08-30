class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        ret = []
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, len(nums) - 2):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        a = nums[i]
                        b = nums[j]
                        l = j + 1
                        r = len(nums) - 1
                        while l < r:
                            c = nums[l]
                            d = nums[r]
                            if a + b + c + d == target:
                                ret.append([a, b, c, d])
                                while l < r and nums[l] == nums[l + 1]:
                                    l += 1
                                while l < r and nums[r] == nums[r - 1]:
                                    r -= 1
                                l += 1
                                r -= 1
                            elif a + b + c + d < target:
                                l += 1
                            else:
                                r -= 1
        return ret