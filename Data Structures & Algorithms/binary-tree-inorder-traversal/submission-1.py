# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, nodes):
        if not node:
            return

        self.traverse(node.left, nodes)
        nodes.append(node.val)
        self.traverse(node.right, nodes)


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        if root is None:
            return nodes
        self.traverse(root, nodes)

        return nodes



        
