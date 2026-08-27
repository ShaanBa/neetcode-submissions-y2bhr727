# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(n1, n2):
            if n1 and n2:
                if n1.val == n2.val:
                    return isSameTree(n1.left, n2.left) and isSameTree(n1.right, n2.right)
                else:
                    return False
            elif (not n1 and n2) or (n1 and not n2):
                return False
            else:
                return True

        if root and subRoot:
            if (isSameTree(root, subRoot)):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return False
        
