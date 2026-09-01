# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # use list for a stack 
        stack = []

        #create pointer called curr which we will use to traverse the list 
        curr = root

        # while the pointer is pointing to a node
        while k != 0:
            while curr:
                # push the node to the stack
                stack.append(curr)
                # move curr to the bottom left
                curr = curr.left
            # so when we exit we will have the lowest val node at the top and at the bottom we will have our root 
            popped = stack.pop()
            k -= 1
            curr = popped.right
        return popped.val