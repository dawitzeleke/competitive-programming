class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        visited = [[0 for _ in range(col)] for _ in range(row)]

        fresh = 0
        time = 0
        q = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append([r, c, 0])

        while q:

            r, c, t = q.popleft()
            time = max(time, t)
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == 1 and visited[new_r][new_c] != 2:
                    visited[new_r][new_c] = 2
                    q.append([new_r, new_c, t + 1])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    return -1

        return time


        
                    


