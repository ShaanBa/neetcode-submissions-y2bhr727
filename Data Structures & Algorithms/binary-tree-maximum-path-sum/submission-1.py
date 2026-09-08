# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] # make the result varialble which will store our sol
        #set it equal to root for now

        def dfs(root):
            # our dfs helper which will compute max sum of split and no split
            # case 1 no node? just return 0
            if not root:
                return 0

            # now we go to the left and right sbtree this is max no split
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # now that we have out lst no splits rst no splits we do the split  now
            # first if its not bigger than 0, we dont even go there

            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            # here is our max value with a split we compare with the result var 
            # hey is this big enough to nbe the new res 
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            # this is not the return though we need to return max of the subtrees no split
            return root.val + max(leftMax, rightMax)# ok for the max no split it is itself plus its max subtree
            # the math is ocurring because the leafs get their roots plus zero and then it bubbles up

        # now use dfs

        dfs(root)

        return res[0]

