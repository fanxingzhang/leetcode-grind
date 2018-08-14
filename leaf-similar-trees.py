# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        b = []
        c = []
        def helper(n, a):
            if n and not n.left and not n.right:
                a.append(n.val)
            elif n:
                helper(n.left, a)
                helper(n.right, a)
        
        helper(root1, b)
        helper(root2, c)
        return b == c