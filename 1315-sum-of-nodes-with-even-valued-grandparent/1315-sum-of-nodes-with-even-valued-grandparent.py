# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total_sum = 0
        
        def dfs(node):
            if not node:
                return
            if node.val % 2 == 0:
                if  node.left and node.left.left:
                    self.total_sum += node.left.left.val 
                if  node.left and node.left.right:
                    self.total_sum += node.left.right.val 
                if  node.right and  node.right.left:
                    self.total_sum += node.right.left.val 
                if  node.right and node.right.right :
                    self.total_sum += node.right.right.val 
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        return self.total_sum 