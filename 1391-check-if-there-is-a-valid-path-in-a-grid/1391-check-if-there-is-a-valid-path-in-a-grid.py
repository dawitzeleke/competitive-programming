class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        row = len(grid)
        col = len(grid[0])
        parent = defaultdict(list)
        rank = defaultdict(int)
        street = {1 : [(0, 1), (0, -1)],
                 2 :  [(1, 0), (-1, 0)],
                 3 :  [(0, -1), (1, 0)], 
                 4 :  [(0, 1), (1, 0)],
                 5 :  [(0, -1), (-1, 0)],
                 6 :  [(0, 1), (-1, 0)]
                 }
        for i in range(row):
            for j in range(col):
                parent[(i, j)] = (i, j)
                rank[(i, j)] = 1
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
                
            return parent[node]
    
        def Union(n1):
            r1, c1 = n1
            
            for dr, dc in street[grid[r1][c1]]:
                new_r = r1 + dr
                new_c = c1 + dc
                if 0 <= new_r <= row - 1 and 0 <= new_c <= col - 1 and (-dr, -dc) in street[grid[new_r][new_c]]:
                    p1 = n1
                    p2 = (new_r, new_c)
                    parent1, parent2 = find(p1), find(p2)
                    
                    if rank[p1] >= rank[p2]:
                        parent[parent2] = parent1
                        rank[parent1] += rank[parent2]

                    else:
                        parent[parent1] = parent2
                        rank[parent2] += rank[parent1]

        for i in range(row):
            for j in range(col):
                Union((i, j))
        return find((0, 0)) == find((row - 1, col - 1))              
                
                
                
                