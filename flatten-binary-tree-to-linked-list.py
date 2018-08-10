# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return
        
        def helper(n):
            if not n.left and not n.right:
                return n
            if n.left:
                n1 = helper(n.left)
                n2 = n.right
                n.right = n.left
                n.left = None
                n1.right = n2
                if n2:
                    return helper(n2)
                else:
                    return n1
            else:
                return helper(n.right)
            
        helper(root)