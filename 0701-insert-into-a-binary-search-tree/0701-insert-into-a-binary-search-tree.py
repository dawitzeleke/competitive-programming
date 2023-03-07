# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def helper(curr, par=None):
            if not curr:
                if val > par.val:
                    par.right = TreeNode(val)
                else:
                    par.left = TreeNode(val)
            elif val > curr.val:
                return helper(curr.right, curr)
            elif val < curr.val:
                return helper(curr.left, curr)
        helper(root)
        return root