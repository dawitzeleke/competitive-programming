"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        self.max_depth = -float("inf")
        def dfs(node , depth):
            if node.children == []:
                self.max_depth = max(self.max_depth, depth)
                return
            for neighbor in node.children:
                dfs(neighbor, depth + 1)
                

                
        dfs(root, 1)
        return self.max_depth