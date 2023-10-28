# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, isLeft):
            if not node:
                return 0
            if not node.left and node.right == None and isLeft:
                return node.val

            leftNode = dfs(node.left, True)
            rightNode = dfs(node.right, False)

            return leftNode + rightNode

        return dfs(root, False)