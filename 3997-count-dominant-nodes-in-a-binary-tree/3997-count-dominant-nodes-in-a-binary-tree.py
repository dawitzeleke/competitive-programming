# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        answer = 0

        def dfs(node):
            nonlocal answer
                

            leftmax = dfs(node.left) if node.left else 0
            rightmax = dfs(node.right) if node.right else 0
            if node.val >= leftmax and node.val >= rightmax:
                answer += 1
            return max(node.val, leftmax, rightmax)

        dfs(root)

        return answer