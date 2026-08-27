# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root

        """# ok so we can say that is both p and q are less than the root then the lca is in the LST
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # if p and q both are bigger than the root then go into the RCA
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # this means that one of p/q is bigger or smaller than the root are is the root itself
        else:
            return root"""
        