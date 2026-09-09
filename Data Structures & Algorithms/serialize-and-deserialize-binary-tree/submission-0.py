# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []
        def preorder(root):
            if root:
                arr.append(root.val)
                preorder(root.left)
                preorder(root.right)
            else:
                arr.append(None)
        preorder(root)
        return "_".join( [str(num) if num is not None else 'a' for num in arr]  )
            

    

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split('_')
        self.i = 0 # pointer that will contain our index we are on

        def dfs():
            if tokens[self.i] == 'a': # do dfs on the  case 1 we are on 'a' which is null
                self.i += 1
                return None # increment the pinter and return none
            node = TreeNode(int(tokens[self.i])) # else we just make a node and add the token to it
            self.i += 1

            #now call dfs again on the nodes left and right

            node.left = dfs()
            node.right = dfs()

            return node # and then return the node (i.e big momma)
        
        return dfs() # and for de serialize just return big momma 


