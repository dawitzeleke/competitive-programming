class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i: i for i in range(1, len(edges) + 1)}
        rank = [1 for i in range(len(edges))]
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
            if find(a) == find(b):
                return [a, b]
            Union(a, b)
        return answer