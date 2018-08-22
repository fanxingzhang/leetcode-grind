# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        def helper(n):
            if not n:
                return
            if not n.left and not n.right:
                ret.append(n.val)
                return
            if n.left:
                helper(n.left)
            ret.append(n.val)
            if n.right:
                helper(n.right)
            
        helper(root)
        return ret