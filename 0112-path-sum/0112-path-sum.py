# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return 0
        queue = collections.deque()
        
        visited = set()
        queue.append((root, root.val))
        visited.add(root)
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                current_node = current[0]
                current_sum = current[1]
                
                if current_node.left:
                    queue.append((current_node.left, current_sum + current_node.left.val))
                    visited.add(current_node.left)
                if current_node.right:
                    queue.append((current_node.right, current_sum + current_node.right.val))
                    visited.add(current_node.right)
                if not current_node.right and not current_node.left:
                    if current_sum == targetSum:
                        return True
            
        return False