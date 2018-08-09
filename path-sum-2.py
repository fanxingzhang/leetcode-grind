# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret = []
        
        def helper(n, s, a):
            if not n:
                return
            if s == n.val and not n.right and not n.left:
                ret.append(a + [n.val])
                return
            
            helper(n.right, s - n.val, a + [n.val])
            helper(n.left, s - n.val, a + [n.val])
            return
        
        helper(root, sum, [])
        return ret