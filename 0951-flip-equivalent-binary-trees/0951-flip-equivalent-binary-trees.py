# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node1, node2):
        if not node1 and not node2:
            return True
        if (not node1 and node2) or (not node2 and node1):
            return False
        if node1.val != node2.val:
            return False
        
        return (self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)) or (self.helper(node1.left, node2.left) and self.helper(node1.right, node2.right))
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        result = self.helper(root1, root2)
        return result