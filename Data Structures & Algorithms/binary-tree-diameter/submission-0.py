# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxPath = 0

        def rec(node):
            if not node:
                return 0
            
            left = rec(node.left)
            right = rec(node.right)
            self.maxPath = max(self.maxPath, left + right)

            return max(left, right) + 1
        
        rec(root)

        return self.maxPath



    
        
        
        

        