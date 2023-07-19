class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        
        
        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)
            
        
        def dfs(node, parent):
            totalTime = 0
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                childnode = dfs(neighbor, node)
                if childnode > 0 or hasApple[neighbor]:
                    totalTime += 2 + childnode
            return totalTime 
        
        return dfs(0, -1)