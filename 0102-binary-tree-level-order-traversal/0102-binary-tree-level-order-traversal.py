# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list)
        def helper(node, level):
            if not node:
                return
            result[level].append(node.val)
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        helper(root, 0)
        j = 0
        res = []
        while True:
            if j in result:
                res.append(result[j])
            else:
                break
            j += 1
        return res