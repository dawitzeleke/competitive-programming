class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        answer = 0 
        visited = set()
        def bfs(r,c):
            queue = collections.deque()
            visited.add((r,c))
            queue.append((r,c))
            diff = [[0,1], [1,0], [-1, 0], [0,-1]]
            while queue:
                ro, co = queue.popleft()
                for dr, dc in diff:
                    rn = ro + dr
                    cn = co + dc
                    if rn in range(row) and cn in range(col) and grid[rn][cn] == "1" and (rn, cn) not in visited:
                        visited.add((rn, cn))
                        queue.append((rn, cn))
                
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r,c)
                    
                    answer += 1
        return answer