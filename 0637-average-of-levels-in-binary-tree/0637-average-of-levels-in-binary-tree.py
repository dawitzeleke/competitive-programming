# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level = defaultdict(list)
        def helper(node, lev):
            if not node:
                return 
            
            level[lev].append(node.val)
            helper(node.left, lev + 1)
            helper(node.right, lev + 1)
        helper(root, 0)
        res = []
        for k, v in level.items():
            if v:
                temp = sum(v)/ len(v)
                res.append(temp)
                
        return res