# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(n, l):
            if not n:
                return [True, l]
            a = helper(n.left, l + 1)
            b = helper(n.right, l + 1)
            return [a[0] and b[0] and abs(a[1] - b[1]) <= 1, max(a[1], b[1])]
        return helper(root, 0)[0]
                