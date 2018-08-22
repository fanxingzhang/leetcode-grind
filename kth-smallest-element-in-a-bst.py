# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ret = 0
        self.c = 0
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        def helper(n):
            if not n:
                return
            if not n.left and not n.right:
                self.c += 1
                if self.c == k:
                    self.ret = n.val
                return
            if n.left:
                helper(n.left)
            self.c += 1
            if self.c == k:
                self.ret = n.val
                return
            if n.right:
                helper(n.right)
            
        helper(root)
        return self.ret