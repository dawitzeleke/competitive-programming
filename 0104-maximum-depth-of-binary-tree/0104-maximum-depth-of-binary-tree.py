# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque()
        depth = 0
        visited = set()
        queue.append(root)
        visited.add(root)
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                
                if current.left:
                    queue.append(current.left)
                    visited.add(current.right)
                if current.right:
                    queue.append(current.right)
                    visited.add(current.right)
            
            depth += 1
            
        return depth