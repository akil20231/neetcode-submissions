# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, nodes):
        if not root:
            return
        
        self.traverse(root.left, nodes)
        self.traverse(root.right, nodes)
        nodes.append(root.val)


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []

        self.traverse(root, nodes)

        return nodes