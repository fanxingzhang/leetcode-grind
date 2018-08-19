# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        ret = []
        q = [[root]]
        while q:
            nodes = q.pop(0)
            ret.append(nodes[-1].val)
            new = []
            for n in nodes:
                if n.left:
                    new.append(n.left)
                if n.right:
                    new.append(n.right)
            if new:
                q.append(new)
        return ret