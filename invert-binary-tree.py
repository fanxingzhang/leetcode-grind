# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def helper(n):
            if not n:
                return n
            temp = n.right
            n.right = helper(n.left)
            n.left = helper(temp)
            return n
        
        return helper(root)