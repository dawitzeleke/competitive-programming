class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row = len(grid)
        col = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != "1":
                return

            visited.add((r, c))

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if (new_r, new_c) not in visited:
                    dfs(new_r, new_c)
        answer = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    answer += 1

        return answer