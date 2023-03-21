# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, current, res):
        if not node:
            return
        temp = current + str(node.val)
        if not node.left and not node.right:
            res.append(temp)
        else:
            self.helper(node.left, temp + "->", res)
            self.helper(node.right, temp + "->", res)
        
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.helper(root, "", res)
        return res
        