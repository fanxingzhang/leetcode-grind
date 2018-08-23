# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        a = [[root]]
        ret = []
        r = False
        
        while a:
            nodes = a.pop(0)
            new = []
            rn = []
            for n in nodes:
                rn.append(n.val)
                if n.left:
                    new.append(n.left)
                if n.right:
                    new.append(n.right)
            if new:
                a.append(new)
            if r:
                ret.append(rn[::-1])
            else:
                ret.append(rn)      
            r = not r
            
        return ret