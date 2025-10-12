# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levelDict = defaultdict(list)

        def dfs(node, level):
            if not node:
                return 

            levelDict[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        
        
        answer = []

        for level, nodes in levelDict.items():
            answer.append([level, nodes])

        answer.sort()

        for i in range(len(answer)):
            answer[i] = answer[i][1]

        return answer
