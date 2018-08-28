# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def helper(n):
            if n in (None, p, q):
                return n
            right = helper(n.right)
            left = helper(n.left)
            if left and right:
                return n
            return left if left else right
        return helper(root)
                