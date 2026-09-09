# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # store the result in an array (scope for recursion), start with root.val
        res = [root.val]

        # define dfs helper that will do our split and non split work
        def dfs(root):
            if not root: # if the node dont exist, return 0
                return 0
            
            # now we do our recursive work going down both subtrees

            lstMax = dfs(root.left)
            rstMax = dfs(root.right)

            # first lets do some handlings for negatived we dont want to include negatives unlesss we have to
            lstMax = max(lstMax, 0)
            rstMax = max(rstMax, 0)

            # now we do our split work which will update the result where we say whats bigger the curr result or the val of plus our left and right max 



            res[0] = max(res[0], root.val + lstMax + rstMax)

            # now we need to compute the return value which is the non split which is similar, its the root + biggest st 

            return root.val + max(lstMax, rstMax)

        dfs(root)

        return res[0]




        