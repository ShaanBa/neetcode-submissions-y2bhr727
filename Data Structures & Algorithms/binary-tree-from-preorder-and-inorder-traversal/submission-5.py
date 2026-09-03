# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ioHashmap = {}
        for i in range(len(inorder)):
            ioHashmap[inorder[i]] = i 
        def buildSubtree(left, right):
            if left > right:
                return
            root = preorder.pop(0)
            dummy = TreeNode(root)

            root_idx = ioHashmap[root]

            dummy.left = buildSubtree(left, root_idx - 1)
            dummy.right = buildSubtree(root_idx + 1, right)

            return dummy
        return buildSubtree(0, len(inorder) - 1)

            
        