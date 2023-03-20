# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    t = 0
    def helper(self, node):
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        self.t += abs(left - right)
        return left + right + node.val
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.helper(root)
        return self.t