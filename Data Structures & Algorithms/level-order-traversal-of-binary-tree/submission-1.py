from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque()
        array = []
        curr = root

        dq.append(curr)

        while dq:
            curr_array = []
            level_size = len(dq)
            for _ in range(level_size):
                curr = dq.popleft()
                if curr:
                    curr_array.append(curr.val)
                    dq.append(curr.left)
                    dq.append(curr.right)
            array.append(curr_array)
        return array[:len(array) - 1]


        