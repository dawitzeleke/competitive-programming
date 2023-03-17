# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node1, node2):
        if not node1 and not node2:
            return None
        val1 = node1.val if node1 else 0
        val2 = node2.val if node2 else 0
        node = TreeNode(val1 + val2)
        node.left = self.helper(node1.left if node1 else None, node2.left if node2 else None)
        node.right = self.helper(node1.right if node1 else None, node2.right if node2 else None)
        return node
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        a = self.helper(root1, root2)
        return a