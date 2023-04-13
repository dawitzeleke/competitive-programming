class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        
        row = len(grid)
        col = len(grid[0])
        self.count = 0
        visited = set()
        def bfs(r,c):
            queue = collections.deque()
            area = 0
            queue.append((r,c))
            diff = [[0,0], [0,1], [1,0], [-1, 0], [0,-1]]
            while queue:
                ro, co = queue.popleft()
                for dr, dc in diff:
                    rn = ro + dr
                    cn = co + dc
                    if rn in range(row) and cn in range(col) and grid[rn][cn] == 1 and (rn, cn) not in visited:
                        visited.add((rn, cn))
                        queue.append((rn, cn))
                        self.count += 1   
                
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    bfs(r,c)
                    self.max_area = max(self.max_area, self.count)
                    self.count = 0
        return self.max_area
            