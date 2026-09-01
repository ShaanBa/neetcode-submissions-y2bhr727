# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node, arr, k):
            if node:
                inorder(node.left, arr, k)
                arr.append(node.val)
                inorder(node.right, arr, k)
            return arr
        
        arr = inorder(root, [], k)
        return arr[k-1]
            
            
        