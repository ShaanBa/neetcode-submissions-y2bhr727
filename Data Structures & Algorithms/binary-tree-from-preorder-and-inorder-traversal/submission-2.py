# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # first setup the mapping (val, idx)
        inorderHashmap = {}
        for i in range(len(inorder)):
            inorderHashmap[inorder[i]] = i 
        

        # now we have our pointers that will help with 
        # narrowing down the inorder array so if the value Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
        # ok lets think for 1 we pass in inorderhashmap[1]

        def helper(left, right):
            if left > right:
                return
            root = preorder.pop(0)
            dummy = TreeNode(root)
            root_idx = inorderHashmap[root]

            dummy.left = helper(left, root_idx - 1)
            dummy.right = helper(root_idx + 1, right)

            return dummy
            
        return helper(0, len(inorder) - 1)

