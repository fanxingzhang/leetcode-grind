# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(n, l):
            if not n:
                return l
            return max(helper(n.left, l + 1), helper(n.right, l + 1))
        
        return helper(root, 0)