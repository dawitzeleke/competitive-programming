# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        
        def solve(root):
            if not root:
                return 
            else:
                solve(root.left)
                result.append(root.val)
                solve(root.right)
            
        solve(root)
        for i in range(1, len(result)):
            if result[i-1] == result[i]:
                return False
        return (result == sorted(result))