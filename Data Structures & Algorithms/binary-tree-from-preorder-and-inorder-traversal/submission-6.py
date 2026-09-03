# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        p_idx = 0

        ioHashmap = {}
        for i in range(len(inorder)):
            ioHashmap[inorder[i]] = i 
        def buildSubtree(left, right):
            nonlocal p_idx
            if left > right:
                return
            
            dummy = TreeNode(preorder[p_idx])
            
            root_idx = ioHashmap[preorder[p_idx]]
            p_idx += 1

            dummy.left = buildSubtree(left, root_idx - 1)
            dummy.right = buildSubtree(root_idx + 1, right)

            return dummy
        return buildSubtree(0, len(inorder) - 1)

            
        