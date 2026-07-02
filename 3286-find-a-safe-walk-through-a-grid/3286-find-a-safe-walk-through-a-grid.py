from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        # Lose health if the starting cell is unsafe.
        start_health = health - grid[0][0]

        if start_health <= 0:
            return False

        # best[r][c] = maximum health remaining when we've reached (r, c)
        best = [[-1] * cols for _ in range(rows)]
        best[0][0] = start_health

        queue = deque([(0, 0, start_health)])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, curr_health = queue.popleft()

            if r == rows - 1 and c == cols - 1:
                return True

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    next_health = curr_health - grid[nr][nc]

                    if next_health <= 0:
                        continue

                    # Only continue if we reach this cell with MORE health
                    if next_health > best[nr][nc]:
                        best[nr][nc] = next_health
                        queue.append((nr, nc, next_health))

        return False