# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = collections.deque()
        visited = set()
        answer = []
        queue.append(root)
        while queue:
            
            size = len(queue)
            total = 0
            for _ in range(size):
                temp = queue.popleft()
                total += temp.val
                
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            answer.append(total / size)
        return answer
             