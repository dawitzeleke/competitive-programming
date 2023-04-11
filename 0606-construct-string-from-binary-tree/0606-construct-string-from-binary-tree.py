# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, node):
        if not node:
            return ""
        left = self.helper(node.left)
        right = self.helper(node.right)
        if left == "" and right == "":
            return str(node.val) 
        elif left == "":
            return str(node.val) + "()" +  "(" + right + ")"
        elif right == "":
            return str(node.val) + "(" + left + ")"
        else:
            return str(node.val) + "(" + left + ")" + "(" + right + ")"
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        self.res = self.helper(root)

        
        return self.res