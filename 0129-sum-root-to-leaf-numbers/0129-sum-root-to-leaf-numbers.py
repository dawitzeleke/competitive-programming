# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, curr):
        if not node:
            return 
        curr += str(node.val)
        if not node.right and not node.left:
            self.max_num += int(curr)
            return
        
        self.helper(node.left, curr)
        self.helper(node.right, curr)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.max_num = 0
        self.helper(root, "")
        return self.max_num