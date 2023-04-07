"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        if not node:
            return None
        def clone(node):
            if node in oldToNew:
                return oldToNew[node]
            
            temp = Node(node.val)
            oldToNew[node] = temp 
            for neighbor in node.neighbors:
                temp.neighbors.append(clone(neighbor))
                
                
            return temp
        return clone(node)