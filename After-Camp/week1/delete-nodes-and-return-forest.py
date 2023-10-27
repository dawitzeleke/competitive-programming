# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, to_delete):
        if not node:
            return None
        node.left, node.right = self.dfs(node.left, to_delete), self.dfs(node.right, to_delete)
        if node.val in to_delete:
            if node.left:
                self.ans.append(node.left)
            if node.right:
                self.ans.append(node.right)
            return None
        else:
            return node
        
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.ans = []
        node = self.dfs(root, to_delete)
        if node:
            self.ans.append(node)
        return self.ans