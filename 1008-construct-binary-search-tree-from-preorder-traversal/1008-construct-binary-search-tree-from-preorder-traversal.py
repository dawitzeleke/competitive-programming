# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, pre):
        if len(pre) == 0:
            return None
        nod = TreeNode(pre[0])
        nod.left = self.helper([n for n in pre if n < nod.val])
        nod.right = self.helper([n for n in pre if n > nod.val])
        
        return nod
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        self.preorder = preorder
        
        return self.helper(preorder)