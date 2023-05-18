class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = {i: i for i in range(1, n + 1)}
        minimum = {i : float("inf") for i in range(1, n + 1)}
        rank = [1 for i in range(n)]
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
                
            return parent[node]
        
        def Union(n1, n2, dist):
            p1, p2 = find(n1), find(n2)
            if rank[p1 - 1] >= rank[p2 - 1]:
                parent[p2] = p1
                rank[p1 - 1] += rank[p2 - 1]
                minimum[p1] = min(minimum[p1],minimum[p2], dist)
            else:
                parent[p1] = p2
                rank[p2 - 1] += rank[p1 - 1]
                minimum[p2] = min(minimum[p2],minimum[p1], dist)
            
        for a, b, dis in roads:
            Union(a, b, dis)
            
        return minimum[find(1)]