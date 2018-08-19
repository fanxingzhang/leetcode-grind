# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ret = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def helper(n):
            if not n:
                return 0
            a = helper(n.left)
            b = helper(n.right)
            self.ret = max(self.ret, a + b)
            return max(a, b) + 1
        helper(root)
        return self.ret