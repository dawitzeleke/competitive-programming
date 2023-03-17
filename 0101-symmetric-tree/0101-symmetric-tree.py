# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, leftroot, rightroot):
        if not leftroot and not rightroot:
            return True
        if (leftroot and not rightroot) or (rightroot and not leftroot):
            return False
        if leftroot and rightroot:
            return leftroot.val == rightroot.val and self.helper(leftroot.left, rightroot.right) and self.helper(leftroot.right, rightroot.left)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        answer = self.helper(root.left, root.right)
        return answer 