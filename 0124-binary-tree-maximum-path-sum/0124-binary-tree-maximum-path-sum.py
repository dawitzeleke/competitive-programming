# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_path = float("-inf")
    def helper(self, node):
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        left = max(left, 0)
        right = max(right, 0)
        self.max_path = max(self.max_path, left + right + node.val)
        return node.val + max(left, right, 0)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.max_path