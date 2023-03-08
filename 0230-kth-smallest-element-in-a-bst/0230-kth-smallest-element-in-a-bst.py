# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        
        def solve(root):
            if not root:
                return 
            else:
                solve(root.left)
                result.append(root.val)
                solve(root.right)
            
        solve(root)
        result.sort()
        return result[k-1]