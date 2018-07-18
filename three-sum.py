class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        sol = []
        for i in range(0, len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                curr = nums[i]
                left = i + 1
                right = len(nums) - 1
                while (left < right):
                    sum = curr + nums[left] + nums[right]
                    if sum == 0:
                        sol.append([curr, nums[left], nums[right]])
                        while (left < right and nums[left] == nums[left + 1]):
                            left += 1
                        while (left < right and nums[right] == nums[right - 1]):
                            right -= 1

                        left += 1
                        right -= 1

                    elif sum < 0:
                        left += 1
                    else:
                        right -= 1
        return sol