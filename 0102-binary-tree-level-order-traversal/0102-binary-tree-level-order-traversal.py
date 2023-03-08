# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def helper(node, level):
            if not node:
                return
            result.append((node.val, level))
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        helper(root, 0)
        result.sort(key = lambda x:x[1])
        res= []
        j = 0
        while j < len(result):
            temp = []
            level = result[j][1]
            while j < len(result) and result[j][1] == level:
                temp.append(result[j][0])
                j += 1
            res.append(temp)
        return res