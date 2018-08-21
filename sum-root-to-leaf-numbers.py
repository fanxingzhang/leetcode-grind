# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.s = 0
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        def helper(n, i):
            i *= 10
            i += n.val
            if not n.left and not n.right:
                self.s += i
                return
            if n.right:
                helper(n.right, i)
            if n.left:
                helper(n.left, i)
        helper(root, 0)
        return self.s
        