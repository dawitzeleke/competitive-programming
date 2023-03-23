# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, node, level, index):
        if not node:
            return
        self.d[level].append(index)
        self.helper(node.left, level + 1, 2*index)
        self.helper(node.right, level + 1, 2*index + 1)
        
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = defaultdict(list)
        self.helper(root, 0, 0)
        res = list(self.d.values())
        result = -float("inf")
        
        for a in res:
            if len(a) > 1:
                result = max( result, abs(a[-1] - a[0]) + 1)
            else:
                result = max(result, 1)
            
        return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    