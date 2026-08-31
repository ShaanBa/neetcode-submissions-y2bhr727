# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # ok now to try to explain this we do dfs on this node so starting at the root
        # if it doesnt exist then return True we got to the leave and its looking good
        # if the if the nodes val is tween min and max then we can go down the tree and do dfs on left and right 
        def dfs(node, min_val, max_val):
            if not node:
                return True
            if min_val < node.val < max_val:
                return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)
            else:
                return False
            
        return dfs(root, float('-inf'), float('inf'))
