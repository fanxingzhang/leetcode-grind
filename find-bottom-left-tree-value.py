# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = root
        q = [root]
        while q:
            ret = q[0]
            new = []
            for n in q:
                if n.left:
                    new.append(n.left)
                if n.right:
                    new.append(n.right)
            q = new
        
        return ret.val