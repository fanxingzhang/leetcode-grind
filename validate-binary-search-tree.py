# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def helper(n, min, max):
            if not n:
                return True
            if n.val <= min or n.val >= max:
                return False
            return helper(n.left, min, n.val) and helper(n.right, n.val, max)
        
        return helper(root, float('-inf'), float('inf'))
        
            