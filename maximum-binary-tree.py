# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 1:
            return TreeNode(nums[0])
        if len(nums) == 0:
            return None
        
        maxNum = max(nums)
        index = nums.index(maxNum)
        root = TreeNode(maxNum)
        root.left = self.constructMaximumBinaryTree(nums[0 : index])
        root.right = self.constructMaximumBinaryTree(nums[index + 1:])
        return root
        