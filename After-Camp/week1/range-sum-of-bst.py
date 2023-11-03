# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def helper(node):
            if not node:
                return 0
            
            temp = helper(node.left) + helper(node.right)
            if node.val >= low and node.val <= high:
                temp += node.val 
            return temp

        return helper(root)