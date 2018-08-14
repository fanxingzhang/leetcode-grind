# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.count = 0
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def helper(n, s, target, d):
            if not n:
                return
            s += n.val
            
            self.count += d.get(s - target, 0)
            d[s] = d.get(s, 0) + 1
            
            helper(n.left, s, target, d)
            helper(n.right, s, target, d)
            
            d[s] = d[s] - 1
        
        helper(root, 0, sum, {0:1})
        return self.count