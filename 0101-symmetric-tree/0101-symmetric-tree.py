# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.issymetric(root.left, root.right)
    def issymetric(self,leftroot , rightroot):
        if rightroot and leftroot:
            return rightroot.val == leftroot.val and self.issymetric(leftroot.left, rightroot.right) and self.issymetric(leftroot.right, rightroot.left)
        return leftroot == rightroot