class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row = len(maze)
        col = len(maze[0])
        queue = collections.deque()
        visited = set()
        visited.add((entrance[0], entrance[1]))
        queue.append((entrance[0], entrance[1], 0))
        directions = [[0,-1], [-1, 0], [1, 0], [0,1]]
        while queue:
            
            current = queue.popleft()
            current_row = current[0]
            current_col = current[1]
            current_steps = current[2]
           
            for dr, dc in directions:
                new_row = current_row + dr
                new_col = current_col + dc
                
                if 0 <= new_row <= row - 1 and 0 <= new_col <= col - 1:
                    if (new_row, new_col) not in visited and maze[new_row][new_col] == ".":
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col, current_steps + 1))

                elif (current_row, current_col) != (entrance[0], entrance[1]):
                    return current_steps
                
        return -1
                    