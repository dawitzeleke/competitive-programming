# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.helper(root)
    def helper(self, node):
        if not node:
            return 
        
        right_subtree = self.helper(node.right)
        left_subtree = self.helper(node.left)
        
        node.right = self.prev
        node.left = None
        self.prev = node

            

        
        
