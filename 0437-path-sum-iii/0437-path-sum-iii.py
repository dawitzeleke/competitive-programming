# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    d = {0:1}
    counter = 0
    def helper(self, node, c_s):
        if node == None:
            return 
        c_s += node.val
        if (c_s - self.targetsum) in self.d:
            self.counter += (self.d[c_s - self.targetsum])
        self.d[c_s] = 1 + self.d.get(c_s, 0)
        self.helper(node.left, c_s)
        
        self.helper(node.right, c_s)
        if self.d[c_s] == 1:
            self.d.popitem()
        else:
            self.d[c_s] -= 1
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.targetsum = targetSum
        self.helper(root, 0)
        return self.counter