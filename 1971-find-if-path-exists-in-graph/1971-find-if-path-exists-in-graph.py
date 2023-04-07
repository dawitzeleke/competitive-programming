class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        connections = defaultdict(list)
        
        for i in range (len(edges)):
            connections[edges[i][0]].append(edges[i][1])
            connections[edges[i][1]].append(edges[i][0])
            
        def dfs(s, d, visited):
            
            if s == d:
                return True
            visited.add(s)
            for c in connections[s]:
                if c not in visited:
                    found = dfs(c, d, visited)
                    
                    if found:
                        return True
                    
        return dfs(source, destination, set())