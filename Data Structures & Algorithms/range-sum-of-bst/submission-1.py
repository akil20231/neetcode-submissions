# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0

        def traverse(n):
            nonlocal total

            if not n:
                return

            if low <= n.val <= high:
                total += n.val

            traverse(n.left)
            traverse(n.right)

        traverse(root)
        return total

