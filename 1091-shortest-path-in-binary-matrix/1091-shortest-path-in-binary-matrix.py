from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        if grid[0][0] == 1 or grid[row - 1][col - 1] == 1:
            return -1
        queue = deque()
        visited = set()
        direction = [[1,0], [0,-1], [0,1], [-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]
        min_distance = float("inf")
        queue.append((0,0, 1))
        visited.add((0,0))
        while queue:
            temp = queue.popleft()
            if temp[0] == row - 1 and temp[1] == col - 1:
                min_distance = min(min_distance, temp[2])
                break
                
            for dr, dc in direction:
                r = temp[0] + dr
                c = temp[1] + dc
                if 0 <= r <= row - 1 and 0 <= c <= col - 1  and (r, c) not in visited and grid[r][c] == 0 :
                    visited.add((r,c))
                    queue.append((r, c, temp[2] + 1))
                    
        return min_distance if min_distance != float("inf") else -1 
        