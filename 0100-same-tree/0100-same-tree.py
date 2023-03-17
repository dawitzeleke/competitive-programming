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
        if (not node1 and node2) or (not node2 and node1) or node1.val != node2.val:
            return False
        return self.helper(node1.left if node1 else None, node2.left if node2 else None) and self.helper(node1.right if node1 else None, node2.right if node2 else None)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        answer = self.helper(p,q)
        return answer