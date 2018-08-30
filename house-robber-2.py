# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(n):
            if not n:
                return [0, 0]
            r = helper(n.right)
            l = helper(n.left)
            a = r[0] + l[0]
            b = r[1] + l[1] + n.val
            return [max(a, b), a]
        
        return helper(root)[0]