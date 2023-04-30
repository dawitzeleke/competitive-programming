# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque()
        depth = float("inf")
        visited = set()
        queue.append((root, 0))
        visited.add(root)
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                current_n = current[0]
                current_d = current[1]
                if current_n.left:
                    queue.append((current_n.left, current_d + 1))
                    visited.add(current_n.left)
                    
                if current_n.right:
                    queue.append((current_n.right, current_d + 1))
                    visited.add(current_n.right)
                if not current_n.right and not current_n.left:
                    depth = min(depth, current_d + 1)
            
            
        return depth