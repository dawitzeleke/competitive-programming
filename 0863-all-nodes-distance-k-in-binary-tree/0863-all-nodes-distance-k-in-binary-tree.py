# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def buildGraph(node, parent):
            if not node:
                return 
            if parent:
                graph[node] += [parent]
            
            if node.left:
                graph[node] += [node.left]
                buildGraph(node.left, node)
            if node.right:
                graph[node] += [node.right]
                buildGraph(node.right, node)
                
        answer = []
        buildGraph(root, None)    
        queue = collections.deque()
        visited = set()
        
        queue.append((target, 0))
        visited.add(target)
        while queue:
            
            current_node, current_dist = queue.popleft()
            if current_dist == k:
                answer.append(current_node.val)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, current_dist + 1))
        return answer