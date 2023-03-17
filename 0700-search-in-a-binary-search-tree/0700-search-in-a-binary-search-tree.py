# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, val):
        if not node:
            return
        if node.val == val:
            return node
        if node.val > val:
            return self.helper(node.left, val)
        if node.val < val:
            return self.helper(node.right, val)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        answer = self.helper(root, val)
        return answer