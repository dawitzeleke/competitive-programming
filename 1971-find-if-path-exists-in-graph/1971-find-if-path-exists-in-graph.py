class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        parent = {i: i for i in range(n)}
        rank = [1 for i in range(n)]
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
                
            return parent[node]
        
        def Union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if rank[p1 - 1] >= rank[p2 - 1]:
                parent[p2] = p1
                rank[p1 - 1] += rank[p2 - 1]

            else:
                parent[p1] = p2
                rank[p2 - 1] += rank[p1 - 1]
            
        for a, b in edges:
            Union(a, b)
            
        return find(source) == find(destination)